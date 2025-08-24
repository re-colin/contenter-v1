import os
import json
from yt import youtube
from environment_variables import video_outputs, json_outputs
from write_outputs_to_json_canvas import write_outputs_to_json
from calculate_nodes import calculate_node_size


# Made to support raw string links
def get_video_data(video_link: str, is_transcription_mode_enabled: bool):

    if isinstance(video_link, dict):
        print("items are a dict.")

    if '\n' in video_link:
        video_link = video_link.split('\n')[0]

    if '\r' in video_link:
        video_link = video_link.split('\r')[0]

    if 'watch?v=' in video_link:
        video_link = video_link.split('watch?v=')[1]

    if '&si=' in video_link:
        video_link = video_link.split('&si=')[0]

    
    video_id = video_link
    curr_node_id = 1
    
    
    video_details = youtube.videos().list(
        part='snippet, statistics, contentDetails',
        id=video_id
    ).execute()

    # video_file = os.path.join(video_outputs, f"{video_id}.md")
    json_file = os.path.join(json_outputs, f"{video_id}.canvas")

    node_object = { "nodes": [] }

    for video in video_details.get('items', []):
        with open(json_file, 'w+', encoding="utf-8") as file:
            json.dump(node_object, file)


    for video in video_details.get('items', []):
        canvas_y = 0
        canvas_x = 2700
        title = video['snippet']['title']
        creator = video['snippet']['channelTitle']
        duration = video['contentDetails']['duration']
        publish_date = video['snippet']['publishedAt']
        description = video['snippet']['description']

        # file_out_name = f"{creator} - {title}" Invalid file name.

        video_data_info = f"""
            Title: {title}
            Creator: {creator}
            Length: {duration}
            Publish_date: {publish_date}
            Description: {description}
        """

        # Write video data to .canvas file
        write_outputs_to_json(  
            file_name= video_id,
            card_text= video_data_info,
            canvas_type= 'text',
            canvas_id= f'V{curr_node_id}',
            canvas_x= 1700,
            canvas_y= 0,
            canvas_width= 800,
            canvas_height= 1000,
            canvas_color= "2"
        )

        curr_node_id += 1
        next_page_token = None
        
        comments_request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            pageToken=next_page_token,
        )

        comments_response = comments_request.execute()

        for comment in comments_response['items']:
            author_name = comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
            comment_text = comment['snippet']['topLevelComment']['snippet']['textOriginal']

            comment_full = f"[{author_name}]:  {comment_text}"

            next_page_token = comments_response.get('nextPageToken')
            if not next_page_token:
                break

            # Write video comments data to .canvas file
            write_outputs_to_json(
                file_name= video_id,
                card_text= comment_full,
                canvas_type= 'text',
                canvas_id= f'V{curr_node_id}',
                canvas_x= canvas_x,
                canvas_y= canvas_y,
                canvas_width= 300,
                canvas_height= 200,
                canvas_color= "4"
            )

            curr_node_id += 1
            canvas_y += 400

            if canvas_y == 2000:
                canvas_y = 0
                canvas_x += 400
                                
        if not next_page_token: 
            break


    if is_transcription_mode_enabled == True:
        
        from transcribe_video import transcribe_video
        print("library loaded. transcribing...")

        video_transcription = transcribe_video(video_id, "small")

        print(video_transcription)

        write_outputs_to_json(  
            file_name= video_id,
            card_text= f"# TRANSCRIPT \n{video_transcription}", 
            canvas_type= 'text',
            canvas_id= f'V{curr_node_id}',
            canvas_x= 100,
            canvas_y= 0,
            canvas_width= 800,
            canvas_height= 1000,
            canvas_color= "7"
        )

        curr_node_id += 1
