Video title: What Big-O notation ACTUALLY tells you, and how I almost failed my Google Interview
 Video ID: gCzOhZ_LUps 
 Channel ID: UCEwhtpXrg5MmwlH04ANpL8A 
 Channel Name: SimonDev 
 Video published at: 2021-05-18T11:00:13Z 
 Date of writing file: 2023-04-27 
 
Description: 
 What is Big-O notation, and what are some misconceptions that even advanced engineers have?

Patreon: https://www.patreon.com/simondevyt

Follow me on:
Twitter: https://twitter.com/iced_coffee_dev
Instagram: https://www.instagram.com/beer_and_code/
Github: https://github.com/simondevyoutube/


In this video we'll talk a bit about big-o notation and analysis, how to understand time complexity, and how it's related to understanding performance. We'll approach this from the mathematical definition, going over the limiting behaviour and talking about the strict definition of big-o. How programmers tend to use Big-O informally, what they mean, and how that differs from the strict mathematical definition. There will be some easy examples to work through, talking about the dominant terms and how/why other terms are dropped. We'll also talk about some of the more subtle aspects of big-o, when/why its good, where it kind of fails things, and cap it off with a story.

https://en.wikipedia.org/wiki/Big_O_notation
https://en.wikipedia.org/wiki/Time_complexity
 

#### COMMENTS:

1: Michael Watercott 
 I am surprised that, when reading f(x), you say &quot;f at x&quot; instead of &quot;f of x&quot;. I&#39;ve never heard it spoken that way before, except in a really specific situation where x literally describes a location or something similar. Do you know where your speech pattern comes from? 

 	Replies: []

2: alexis miller 
 The word &quot;faster&quot; was the confusing thing here, there was a lack of quantification on what you were talking about, the functions or their values... 

 	Replies: []

3: Thotaro Joestar 
 &quot;If data plan A costs $1000 every month plus $0.1 per GB while plan B costs $10 every month plus $1 per GB plan B might make more sense if we don&#39;t browse the web that often&quot;<br><br>&quot;You don&#39;t understand big-O&quot;<br><br>What a douchebag lmao 

 	Replies: []

4: nG227 
 A good example is standard library implementations of sorting -- many libraries use a hybrid &quot;introsort&quot; type algorithm, which uses quicksort most of the time, but insertion sort on small arrays because it&#39;s faster (it also will switch from quicksort to heapsort in certain cases, typically when the depth of the recursion becomes large). And of course, insertion sort is O(n^2) compared to the expected O(n log n) for quicksort. 

 	Replies: []

5: MorTobXD 
 I would have just straight up reported him for being incompetent. 

 	Replies: []

6: Syncrossus BAR 
 That interviewer was an idiot. I can&#39;t tell you the number of times my students smugly turned in an algorithm that performed much better than the one seen in class on the small inputs they tested only for it to slow to a crawl at scale. 

 	Replies: []

7: Nerketur Kamachi 
 It&#39;s funny because in the end you were both right, you just didn&#39;t have the terminology correct.<br><br>O(log(n)) is faster than O(n)<br><br>Buuuut!  A function that is bound by O(n) can sometimes perform faster than one bounded by O(log(n))  what you were incorrect about was &quot;oh, that means O(n) can be faster than O(log(n))!&quot;<br><br>That said, the interviewer was a jerk.  You weren&#39;t wrong, you just didn&#39;t use the right terminology.  Strangely, I&#39;m certain that is why you were hired.  XD 

 	Replies: []

8: anubhav singh 
 sound is too soothing man 

 	Replies: []

9: Diconica Bastion 
 Yep lots of so called programmers put way to much stock into Big-O. To be clear it doesn&#39;t have to just be small sets that can be optimized better. Even very large sets can still often perform vastly different. I say that because my datasets tend to be in the 10^18 range of late. Big-O isn&#39;t worth a thing when it comes to finding faster methods of dealing. All big O is good for is comparing similar methods that are &quot;highly&quot; related to each other. 

 	Replies: []

10: John McLeod VII 
 Ive written code that used bubble dirt because we knew two things about the data.  There were at mist 256 entrues, and the data was almost always starting nearly sorted, so just a handfull of passes would be required for the sort (often one or two were enough).  <br><br>I&#39;ve also written code where we knew that there would be millions of records to sort, with no guarantees about order.  Heap sort wins.<br><br>I&#39;ve also written code where the data had to be maintained sorted with millions of records.  Balanced binary trees win. 

 	Replies: []

11: Vagrant 
 These interviewers are the types of guys who name their variables meaningless single characters. If I ever interview someone and give them a real-world problem (which is the only useful type of problem. Academic coding questions are objectively garbage), it would be a huge red flag to see them name vars i, j, k, l, etc. 

 	Replies: ['SimonDev', 'Smaller variable names run faster.<br><br>jk']

12: Vagrant 
 I think this is the mark of a good engineer vs a hobby programmer. You need to think about all aspects of the system you&#39;re building, including what/how much data your functions are expected to process, and that&#39;s where big-O isn&#39;t always the best measure of an optimized system. I would never want to work for a company that just wants me to write functions that do things and then throw it over the wall, I want to know the ins and outs of the entire pipeline in order to make informed decisions on how to design, implement, test, and maintain the system. 

 	Replies: []

13: Lupirite 
 Duude... I was totally thinking about this same exact thing like yesterday... I love it when I just randomly think of something interesting and find someone else talking about that same thing. 

 	Replies: []

14: Sandpiper B F 
 Really upsetting that the interviewer was wrong and completely unreceptive to your explanation... which he should have understood if he thought about it for a few minutes. 

 	Replies: ['SimonDev', 'I worked at Google for a long time, some really great engineers there, but some giant egos there too.']

15: Xavi 
 It is important to know what regime you are targeting before assessing the best algorithm. Some algorithm can be eventually better than another. But is that “eventually” practical? 

 	Replies: ['SimonDev', 'Galactic algorithms']

16: RonJohn63 
 <a href="https://www.youtube.com/watch?v=gCzOhZ_LUps&amp;t=8m06s">8:06</a> You were right, and he was wrong.  It&#39;s why bubble sort is better for small (like 10-20 element) arrays. 

 	Replies: []

17: Mark Crawford 
 Ah. What a shame. You know you go in there looking up to these people thinking they radiate expertise, just to find they are as error prone as the rest of us. Anyone willing to take a second to visualize O(n) and O(logn) can intuit that if there is a point of intersect on their graphs, then there are two sides to that intersection, each with its own story to tell. 

 	Replies: []

18: yt20xxx06yt 
 You&#39;re absolutely correct !!! 

 	Replies: []

19: Enderman 
 Looks like this man was just an asshole. I haven&#39;t ever been interviewed, but why wouldn&#39;t the guy just correct you instead of saying &quot;no, that&#39;s wrong&quot;? I&#39;d be really pissed if someone just said I&#39;m wrong without explaining the details on why I am. Clearly, it was just a nitpick, but even still. Is there any reason to drown a newcomer if they&#39;re obviously smart enough to be a decent programmer? 

 	Replies: []

20: Quinn Bero 
 This is a fantastic video, and the way it was broken down visually along side the explanation of the definitions was very helpful 

 	Replies: []

21: Clinton Billedeaux 
 Great example of being thorough is regarded as bad and generalizations are regarded as good. 

 	Replies: []

22: Wouter-Jan Kok 
 Maybe the Google Engineer tried to make you, question your own level of understanding. Doing some basic psychological trickery. As it would break most, of those who fake their knowledge. 

 	Replies: ['SimonDev', 'Maybe, but that&#39;s definitely not a supported interview tactic at Google, so he&#39;d be outside the bounds of reasonable behaviour']

23: Omni 
 That interview shocked me.. It&#39;s an unambiguous example of people taking generalizations as facts that lack nuance. 

 	Replies: []

24: Game Channel 
 From looking at a bunch of things that google has produced, such as the Angular 2+ framework and the google analytics APIs, I would say that google is full of idiots. My impression of the average google developer is that they code 10000 lines first, making an API as complex as possible, and save the design time for after they&#39;ve made 1000 mistakes and it&#39;s too late to fix. 

 	Replies: ['SimonDev', 'Heh, it&#39;s sort of the other way around. It&#39;s hard to write any code at Google (or really any other big company). You spend endless time in design docs arguing over every last detail with everyone, and then finally implement &quot;something&quot;, usually a compromise that makes the people (who can promote you) happy. Then you take off before it comes crashing down.']

25: Taliyah Pottruff 
 If you know the domain then its probably generally better to calculate the run time at the maximum for that domain instead of just falling back on Big-O. Big-O shines with unknown domains, it is not a one size fits all tool. 

 	Replies: []

26: Tim de Jong 
 So your interviewer wasn&#39;t only wrong, he was also an asshole about it? 

 	Replies: []

27: ABaumstumpf 
 Had a performance-problem in production-code that i could trace back to a customised container.<br>They wanted to be &quot;smart&quot; and speed up checking if it contains a value or not. But if you have a vector with only like 10 elements at most and only ever look up 3-4 elements inside than doing a std::sort and std::binary_search is a lot slower than just std::find. 

 	Replies: []

28: SuperNovaJinckUFO 
 Never in my life did I expect to be taught about big O notation by Eeyore 

 	Replies: []

29: blightmoon 
 To be fair, context matters, and at the scales that Google does things, the nitty gritty is just noise.<br><br>Your special ability is in connecting the tech guys and the finance guys especially on small/pilot projects. 

 	Replies: ['SimonDev', 'I recall internally an engineer saved a huge amount of money once by optimizing memcpy. At Google&#39;s scale, it was worth $$$$$.<br><br>But back to the interview, context does matter, which is why I framed it by calling out Google&#39;s scale, but also talking about micro scales. In reality, an interview is about 1 thing, assessing a candidate&#39;s abilities, so discussions SHOULD be about exploring what they know and don&#39;t know, the depths of their knowledge.']

30: The Eclectic Dyslexic 
 If anyone questions you about this again, just point to Tim sort changing to insertion sort instead of merge sort when sublists get small enough. No one in their right mind is going to claim Tim sort is wrong. 

 	Replies: []

31: Google User 
 Finally someone agrees with me 

 	Replies: []

32: Moira Goree 
 I have been confused about this concept for a long while now and you explained it beautifully 

 	Replies: []

33: King Killer 
 I wouldn&#39;t have gotten the job after that interview, I&#39;d have responded to &quot;sounds like you don&#39;t understand big O&quot; with &quot;I&#39;m sorry, I didn&#39;t realize you don&#39;t understand basic math.&quot; 

 	Replies: ['SimonDev', 'I don&#39;t think anybody would blame you heh']

34: pihi42 
 Perhaps your interviewer was being evaluated himself? Would be ironic, him being the asymptotically worse case but having the advantage of small numbers in the situation! 

 	Replies: []

35: rogermwilcox 
 I DID fail my Google interview in the early 2000s, by getting the Order of a search algorithm wrong.  (I guessed it was O(n log n). It was actually O(n).)<br><br>This interview happened BEFORE Google went IPO.  If I&#39;d gotten the Order right, I&#39;d be a multimillionaire now.  😕 

 	Replies: ['SimonDev', 'Yeah I can&#39;t imagine how rich those guys are, especially if they held the stock for a while']

36: Dragonax 
 I have background in physics and it baffles me how those engineers don&#39;t get it, just make plot to see one thing can be faster than other for small numbers. This is basic math that different functions grow differently 

 	Replies: []

37: THE16THPHANTOM 
 nothing worse than debating a robot who values are constant. my friend you&#39;ve memorized the book by heart but you understand nothing. you are a record. you have become the book. should never become the book. 

 	Replies: []

38: Marcelo Andrade 
 It&#39;s hard to put an upper bound on how good this video is. 

 	Replies: []

39: jimmy Wey 
 the sketch-animations are a great aid to the narrative. I am liking the idea at the end and how it relates to intuition, <br>since we keep in mind what is relevant and what resonates, and leave behind the irrelevant bits. 

 	Replies: []

40: apburner1 
 I can take anyone seriously when they can&#39;t pronounce a simple word like &quot;of&quot;. 

 	Replies: ['SimonDev', '@apburner1 :)', 'apburner1', '@SimonDev Just trolling for giggles, no offense intended.', 'SimonDev', 'That&#39;s tough but fair']

41: aquiace 
 It wasn&#39;t that you were wrong, you just signaled which side of the battle line you were on 

 	Replies: []

42: Lekhaka Ananta 
 If you&#39;re a software engineer, and not a software theorist (or software armchair-theorist), then your Big-O calculations need to be confirmed with empirical measurements anyway, so getting stubborn about a theoretical value is kind of pointless. 

 	Replies: ['SimonDev', 'At the end of the day, the profiler tells you exactly how it ran anyway']

43: roax206 
 Then you realize the processor is loading a new page on the hard disk for each operation because your memory management is so poor and what could have been done in 5 seconds from the registers with a higher order algorithm is now taking 5 days. 

 	Replies: []

44: Oleg Ostanin 
 You are technically correct. The best kind of correct. 

 	Replies: []

45: I. Wyrd 
 Thank you for your video, and congratulations on surviving that interview despite the part where it went off the rails. 

 	Replies: []

46: Soninho Dev 
 Hey, i remember something similar, i remember i made a little rpg game in rpg maker, and in that game every single character grew exponentially stronger when they leveled up, i then made a character who, would start out 10x weaker than the rest, but would became stronger faster, i was reminded of that character by the curve at the end of the video :) 

 	Replies: []

47: Shahar Har-Shuv 
 It&#39;s really disappointed to hear that &quot;google engineers&quot; (that supposedly have a good understanding of computer science) shows a significant lack of understanding of it when they are interviewing. <br>That&#39;s a really good point though nonetheless, since in the &quot;academy&quot; that only teach you to analyze performance based on &quot;order of&quot;, while a lot of time it doesn&#39;t matter in reality. I started to get into the habit of actually checking performance in practice and see what is based for my particular use case. This is even more important if you&#39;re working with high-level languages in which the implementation details are not clear to the consumer, so it&#39;s not obvious what is faster, and developers often get it wrong. 

 	Replies: []

48: JonMcFluffy 
 another thing to consider is that while a linear search is O(n) and binary search is O(logn), you can linear search an unsorted array but you cant binary search an unsorted array. the fastest sort thus far i believe is a radix sort at O(n). so the binary search of an unsorted array is O(nlogn) which is technically slower than a linear search. which could be useful if you are searching a inherently randomizing situation like game objects and their positions and determining what &quot;chain lightning&quot; should chain to next. 

 	Replies: []

49: JonMcFluffy 
 in my comsci fund 3 class we had to write a more efficient sorting algorithm than n^3 (the task at hand was to sort pixels in an image line by line, using like its red value or something) and i technically wrote an O(n) sorting (similar but not radix sort). thing is even with sorting 405,000 pixels the O(n) sort was slower because it required the creation and run through of a 4GB array.<br>i just implemented a heap sort for the lab which got me a 100 but in class just to goof around on a slow week my professor actually attempted to implement my sort. heap sorts ran in like 16ms and mine took 4,000. this was on a very small image, like 635x640. we then tried it on a 3000x3000 image and the heap sort ran in 600ms while my sort took 10,000. so it seems like a failure yet the heap sort went up by 37.5x times longer while my sort only went up by 16x. EVENTUALLY my sort would have worked better but only on images that are 100,000x100,000 or something dumb lmao. 

 	Replies: ['SimonDev', 'Sounds like you stumbled onto your own galactic algorithm: <a href="https://en.wikipedia.org/wiki/Galactic_algorithm">https://en.wikipedia.org/wiki/Galactic_algorithm</a>']

50: Anony Mousse 
 One of the first things I learned about algorithmic complexity when I was just starting out is that small scale and large scale are quite different. It&#39;s why the standard method for implementing a quick sort is to use insertion sort under a certain threshold. It&#39;s obvious how this concept can be applied to many things, but I guess they didn&#39;t send someone who knew what they were doing to interview you. 

 	Replies: ['SimonDev', 'I feel like a lot of people have made this mistake, but just aren&#39;t willing to admit to it']

51: proosee 
 Apart from the subject, I hate when interviewer doesn&#39;t have humility to admit he doesn&#39;t know everything and might be wrong, had few examples of that being an interviewee and it&#39;s so frustrating because you a subject in that situation, so it feels unnatural that in fact the interviewer might be wrong, but it <b>can</b> happen, because we are only humans.<br>Eventually, I learned that this kind of behaviour is just a sign of bad company culture - engineer without a doubt is just poor engineer in my opinion and if the only thing deciding who is right is seniority or position in the company then it&#39;s just toxic and over time it will suck out all of your morale. 

 	Replies: []

52: decky1990 
 Thank you for the video! The maths is where it’s at 

 	Replies: []

53: HansLemurson 
 I was a TA in a Computer Science class a few years ago, and when I did a presentation on BigO notation, I made a point to remind people that there&#39;s there&#39;s always (at least) a constant k scaling up the time costs of one algorithm or the other.<br><br>For example, k*x &gt; x^2 when k is very large.  I illustrated this by drawing a very large letter &quot;K&quot; on the board in front of the formula. 

 	Replies: []

54: Brynjard Øvergård 
 That Constant expression time thing is really interesting, this is why you see a lot of bubble sort used in for example sorting sprite visibility order, shaders, etc), and even when the numbers of elements get large, the memory access model might make it slower than a algorithm with worse scaling, yet with more beneficial memory access, even way past where they should&#39;ve switched places.<br><br>Which just basically all boils down to the usual mantra of performance: Test it! 

 	Replies: []

55: Dante Lee 
 brilliant video, thanks for the insight! 

 	Replies: []

56: Nanospeed 
 why can&#39;t we just say how about lets google this real quick and confirm who is right? 

 	Replies: []

57: monsterrancher1 
 big o its show time! 

 	Replies: []

58: Woeden 
 Great lecture ty 

 	Replies: []

59: Robert DeCaire 
 What I&#39;m getting from this video is that Google engineers are overrated, and the company&#39;s reputation is more like mythology than anything earned. 

 	Replies: ['SimonDev', 'Heh maybe, if that&#39;s what you want to get out of it. What I saw was that even experienced engineers can misunderstand basic things, stay humble.']

60: ronomgenuff 
 I love this so much....... The way you explained it all was exactly how my brain absorbs it lol 

 	Replies: []

61: Don Wald 
 lol moron Ph.D. 

 	Replies: []

62: Kevin Malone 
 How I view it is, Big-O is only concerned with scalability. Scalability is only one dimension of performance. 

 	Replies: []

63: Shan S 
 I hate it how many people out there act like your interviewer. They just function based on little knowledge they&#39;ve engrained into their brains, and when someone goes into details to tell them it is not always the case they just ignore it because they have &quot;read&quot; about it much before you did. No, they&#39;ve just read the basics or how it works in majority of the cases. Like yes, Newtonian gravity wasn&#39;t wrong, but not in all cases. 

 	Replies: []

64: Griffolion 
 Let&#39;s hope the idiot that interviewed you was one of the laid off staff. What a tool. 

 	Replies: []

65: SLED leohja 
 I’m late to the party but this video is really great.<br><br>I think people forget that algorithms are tools in a toolbox. Having a system that can intelligently switch between these tools depending on the task at hand is much better than just using Binary Search and discard everything else because “O(logn) says it’s better”. 

 	Replies: []

66: TesserId 
 The one time I had occasion to write a sort algorithm of my own (in VBA), the arrays I was sorting I knew, a priori, were never going to have more than about four items (in fact that may literally have been the limit, can&#39;t remember why).  There was no way I was going to bother looking up a fancy sorting algorithm and did the first algorithm that I could do from memory.  I totally sympathize with that interview situation. 

 	Replies: []

67: Timmeeyh 
 So what to do then?<br><br>Should we sift through for example sorting algorthm implementations A and B, produce polynomial expressions and then find the ranges for which one is better than the other? 

 	Replies: ['SimonDev', 'If you&#39;re optimizing for performance, yeah you might do that.']

68: Jared Cramsie 
 Showing someone a page on &quot;Galactic algorithms&quot; is good way to convince them that time complexity is not always a good indicator of expected performance. 

 	Replies: []

69: Chrundle the Great 
 I had a situation like this at work dealing with an 8pt FFT ( O(Nlog(N)) ) vs. a 5pt DFT ( O(N^2) ). Funny how things pop up on your feed when they&#39;ve recently come about in your life haha 

 	Replies: []

70: Valko Puhelin 
 Love how this was a long way of saying, &quot;you know that thing years ago, I was right!&quot; 

 	Replies: ['SimonDev', 'I&#39;m often wrong, so it&#39;s important to hang on to the few times I&#39;m right.']

71: Emesh 
 Maybe that Google engineer was testing your ability to stand up to authority figures when you know there&#39;s a problem?<br><br>That&#39;s what I&#39;m hoping, anyway. Google has a lot of my data. 

 	Replies: ['SimonDev', 'Google has everyone&#39;s data :P<br><br>Maybe, but if they&#39;re doing that, pretty sure it&#39;s not recommended practice for conducting an interview at Google. I was also at Google for 7 years, did the interview training, did many interviews. Candidates are stressed enough, I did my best to put them at ease to give them their best shot.']

72: Mitchell Dale 
 I came into this video thinking maybe there was some additional nuance to Big-O that I wasn&#39;t aware of, instead I learned that interviewers at Google don&#39;t necessarily know what they&#39;re talking about. Excellent breakdown of how Big-O works. 

 	Replies: []

73: jason marshall 
 Did you ever attempt to change the culture on this topic? 

 	Replies: ['SimonDev', 'I ended up mentoring junior engineers, apparently I&#39;m good at teaching and explaining things. One thing I did mention often was this story, mostly just to mention that it&#39;s ok to be wrong, keep an open mind. Google is a huge place though, so best most people can do is have an effect on the few people around them.']

74: jason marshall 
 I had a very similar conversation during my Google interview. Did not get the job. <br><br>See also winnowing C, which is high difficulty low return work but sometimes crucial for a sale or profit margin. 

 	Replies: ['SimonDev', 'That&#39;s too bad, their interview process really does suck sometimes.']

75: Paweł Mateusz Bytner 
 You sometimes are too competent to answer the question &quot;correctly&quot; according to the questor&#39;s intent.<br><br>I had a question in an interview for a junior position to write an algorithm performing multiplication without built-in multiplication operator. So I wrote a line of pseudocode:<br>return +/- exp(log|a|+log|b|)<br><br>Interviewer had no idea if that was correct, he actually wanted to check if I knew how to write a loop and conditional. 

 	Replies: ['SimonDev', 'Hah, I love it when an interview candidate can show me something new.']

76: Raphael Morgan 
 that interviewer sounds like the average StackOverflow user tbh 

 	Replies: []

77: Vuk Kulvar 
 if (sizeof(data) &gt; big_threshold) useB(data); else useA(data); 

 	Replies: []

78: bozimmerman 
 Awesome point, well presented.  Five Stars A+.<br>. 

 	Replies: []

79: Edward 
 That interview story was irritating. I&#39;m a mathematician and try to emphasize the same points you made in this video to my students when we cover big-O. Your video was very well explained! 

 	Replies: []

80: John Snow 
 Big-O actually tells you what it tells you by definition. No more, no less, nothing tricky here, just read and think. The story about Googler is not about math vs tech, it is just about unprofessionalism of an interviewer ) 

 	Replies: []

81: James Wasson 
 Big theta is actually the descriptor that should be used for the average time an algorithm takes. Please don&#39;t use big O for that. 

 	Replies: []

82: austin 
 my data structures class didn&#39;t come close to giving this kind of detail and its unsettling 

 	Replies: []

83: Z-Statistic 
 How much does scale checking affect O()? Like, if algorithm 1 perform better than algorithm 2 from 0 &lt; k &lt; 1200 but then algorithm 2 is better for k &gt; 1200, how much does it change the time requirement to check for the scale of inputs and selecting the appropriate algorithm? 

 	Replies: ['SimonDev', 'Cost of a branch really. I&#39;ve been meaning to make a video about branch prediction, but it&#39;s a known cost on each set of hardware, on the order of 1-2 dozen cycles (not at all exact, and will vary a lot). Code in general is littered with branches already, so another probably won&#39;t change anything.']

84: Cavan P 
 Big-O means he&#39;s a keeper 

 	Replies: []

85: Graco Espinoza 
 Great voice, I love it 

 	Replies: []

86: Artem Kotelevych 
 you could&#39;ve ask that google engineer  his opinion on how quick sort is implemented in variety of languages and why does it switch to a &quot;slower&quot; algorithm when the array part length is small enough instead of just dividing till you have an array of 2...<br>maybe they just don&#39;t know something he does... 

 	Replies: ['SimonDev', 'No doubt there&#39;s a million things I could have done, in retrospect. I&#39;m not unhappy how I managed it though, but there are many suggestions here that if I&#39;d been quicker on my feet, I could have used instad.']

87: King Acrisius 
 So...the interviewer was just wrong? I&#39;m a bit confused by this video, I already knew everything you said and assumed you were going to put some gotcha that explains where you went wrong, but it seems like you were entirely in the right. Am I missing something or is the conclusion that you were actually correct and the interviewer was wrong? 

 	Replies: []

88: Aidan Xavier 
 If that&#39;s how you handled the interview, it shows some really great character, that you would stay calm and be sympathetic to the misunderstand of someone shutting you down like that, especially in a nervous situation like an interview. 

 	Replies: []

89: Pedro 
 Not eveyone quite gets the simple concept that complexity does not regard actual measurements of time or memory, but the assymptotic behavior of a function.<br>f(n)=1_000_000_000  is O(1)<br>g(n)=0.0001n               is O(n)<br>f(n) has a lower complexity than g(n), but it doesn&#39;t mean it will run faster (or allocate less memory) than g(n) for any sensible input case. 

 	Replies: []

90: TcheQ _ 
 A guy I work with just got into AWS and told us he had 7 interviews, so sounds similar to your scenario. In my work his main skill is poorly written SQL and lifted python to write from files.  I guess if that&#39;s the quality of candidate big tech likes to recruit it&#39;s no surprise you got in even though you hated yourself.  The guy interviewing you would have understood you could just look it up later and realise your mistake, and the fact you actually had an interest or rudimentary understanding of the concept rather than nothing would have counted for more. 

 	Replies: ['SimonDev', 'Or he&#39;s pretty good at solving algorithms &amp; datastructure style questions on a white board, which is separate from what he does at work.']

91: Jeremy Lakeman 
 I&#39;m vaguely reminded of a white paper about using some novel non-binary tree for evicting data from a proxy cache. Because it beat the best textbook tree for that use case. Why? Because this function only runs slowly in a background thread, when it is guaranteed that all elements of the tree will have been swapped to disk. 

 	Replies: ['SimonDev', 'I&#39;d be interested if you found it']

92: David Pressley 
 I saw what you did with the Office Space reference. Nicely done 

 	Replies: []

93: Christoph Rackwitz 
 Hard to say what was going on with the interviewer. Either he had a brain fart, or he was incompetent, or he was testing how you would handle a peer or authority figure being wrong or unreasonable.<br>I&#39;ma go with &quot;incompetent a**hole&quot; because Google&#39;s hiring is dysfunctional. 

 	Replies: []

94: Larry 
 That google engineer is an idiot. Should be fired. How is he ever going to learn and get better with an attitude like that. Pathetic really 

 	Replies: []

95: PatManGuy 
 I love being taught math/algorithms by Bob Belcher 

 	Replies: []

96: KingGrio 
 Wait, a whole video was needed to clarify something you should learn in maths class somewhere in your bachelor studies ? I was expecting some kind of plot twist here. 

 	Replies: ['SimonDev', '&quot;IF&quot; you did bachelor studies, there&#39;s a lot of self taught devs out there who make these kind of mistakes. I tend to take the attitude that, if you already knew it, great! If you didn&#39;t, no sweat, here it is, let&#39;s understand it.']

97: TalysAlankil 
 you mean people who work at google aren&#39;t magically smarter than everyone else? wild /s<br>seriously though. perfect dunning kruger in effect. dude was wrong but assumed you were wrong instead. 

 	Replies: ['SimonDev', 'I dunno, I heard over and over from people at Google that they were the smartest in the world. /s']

98: Aaron Bredon 
 Occasionally, based on context, an O(x²) operation like bubble sort, will reliably outperform an O(nlogn) operation like merge sort, regardless of the size.<br>One example - you have a huge list that is almost sorted. You know that one entry was added to the end of the list recently. You don&#39;t know where it belongs. A properly written bubble sort will get the list in sorted order in O(n) time, despite the fact that bubble sort is an O(n²) algorithm. A merge sort will still take O(nlogn) time, with a significant extra load applied to set up.<br>Knowing the situation changes the relative speed of operations. 

 	Replies: []

99: Undamaged 
 Cast in the name of god, ye not guilty. 

 	Replies: []

100: NyOS Gomboc 
 I know that Bubble sort is slow (O(n^2)), but I was perfectly happy to use it on an Arduino to sort the results of 3..5 thermometers (and use the 2nd largest). Code complexity matters as well. 

 	Replies: ['SimonDev', 'Yeah, something else a lot of devs don&#39;t understand, the more senior you get, the more multidimensional the problem becomes. You&#39;re balancing performance, memory, time constraints, maintainability, etc..']

101: Scott Duckworth 
 I had a similar interview experience at a large network storage appliance company. The interviews went well until I had this exact conversation with the hiring manager. I was rejected. A year later I was recruited by and hired by Google, where I&#39;m still at today, over 8 years later. 

 	Replies: ['SimonDev', 'Yeah, interviews are really hit &amp; miss. Glad to see you&#39;re settled in at Google, how is it these days? I miss Memegen when I&#39;m bored sometimes heh']

102: Grant Peterson 
 It is really easy to see how this assumption that lower time-complexities doesn&#39;t hold up at smaller scales.<br><br>Let&#39;s say we have an array of 3 elements, defined as x = [1, 2, 3]. We know that x is sorted from smallest to largest, and we need to know what the index of the element marked &quot;3&quot; is.<br><br>First we do a simple search from start to end O(n), and the computer does the following:<br>Checks element 0.<br>Increment<br>Checks element 1<br>Increment<br>Checks element 2<br>return 2, since x[2] == 3<br><br>Now let&#39;s look at a binary search O(log(n)):<br>Set 0 as the left bound of the search<br>Set 2 for the right bound of the search<br>Add right and left bounds together<br>Divide this by two<br>Check divided index<br>Since its smaller, set left bound as that index plus one<br>Repeat above steps, this time return index since it is equal to 3<br><br>Clearly the second method has much more &quot;steps&quot; (even ignoring the fact that division is much more expensive to a CPU than addition/incrementation). Big-O is only a limit as n -&gt; ∞ 

 	Replies: []

103: LeetHaxington 
 What&#39;s the difference between Big-O Notation and Big O Tires? 

 	Replies: ['SimonDev', '... so what is the difference?']

104: Gringohuevon 
 Nice 

 	Replies: []

105: Tom B 
 Well-Done &amp;;<br>If I ever take-over the-world, you&#39;re hired ;). 

 	Replies: ['SimonDev', 'Can I get my own country?']

106: ayesaac 
 My favourite demonstrative example of this point is sleepsort. 

 	Replies: []

107: Akash Garg 
 Me to supervisior: So I have this thing, I&#39;m stuck tho because the current idea is O(n^2) and I am fairly certain it can be made O(n log n) but I ...<br><br>Supervisor: Dude, STFU, just make it work man I don&#39;t care. <br><br>Never optimize first. 

 	Replies: ['SimonDev', 'Unless that&#39;s your job :)']

108: Lyri Metacurl 
 <a href="https://www.youtube.com/watch?v=gCzOhZ_LUps&amp;t=3m15s">3:15</a> but you just said that any function f that overtakes another function g means that function g is of the order of function f, so you can indefinitely say any function is of order whatever higher than it. 

 	Replies: ['SimonDev', 'Yep, something that O(n) is also O(n^2) and O(n^3)']

109: Bertram Stier 
 That same scenario is way too often happening in all kinds of fields. bigger statements that are correct in certain scenarios are induced to be correct at other scenarios. aaaaand thats just not true. People need to differentiate in relevant cases. 

 	Replies: []

110: Roger Levasseur 
 As I can remember Big-O notation being presented in the algorithms class (back in the 80s for me), I do recall the instructor touching upon what SimonDev is presenting.  It was select your algorithm to your needs. If your data set is small, go ahead with the bubble sort.  it was probably easier to implement, test, and validate over a more complex sorting algorithm. 

 	Replies: []

111: FancyUnicorn 
 Cast in the name of God, Ye not guilty 

 	Replies: []

112: Nikil Ragav 
 I don&#39;t think your explanation works very well unless you already have some idea of big O. For example, your binary search introduction kind of assumes the person has seen it before. But I really liked your explanation at the end on small n! 

 	Replies: []

113: Waffles Enjoyer 
 while it doesn&#39;t sound like the case here, sometimes a lightly argumentative interviewer (without going too far, ofc) can really be fishing for your interpersonal behavior, moreso than genuinely arguing matters of fact.  this can also be the case when you&#39;re given what is secretly intended to be an impossible or unreasonable challenge. 

 	Replies: ['SimonDev', 'Yeah, I can see that.']

114: jmw150 
 I am surprised they hired you. This is freshman level stuff. 

 	Replies: ['HaZe', '@SimonDev I don&#39;t think this guy actually finished the video or paid attention.', 'SimonDev', 'That&#39;s an odd way of looking at it, are you suggesting I shouldn&#39;t have gotten hired because I disagreed with the interviewer? Or because I decided correcting him wasn&#39;t worth potentially tanking my own interview?']

115: Shizumi Munyu 
 A lot of sorting algorithms&#39; time complexity (and thus efficiency) can highly depend on what you know about the expected input data.<br><br>If you&#39;re dealing with highly sorted data (e.g. you&#39;re appending a few items to an already sorted list), then insertion sort will vastly outperform any &quot;efficient&quot; algorithm like quicksort or mergesort despite technically being O(n^2).<br>If comparisons are costly for whatever reason, then mergesort will outperform quicksort due to making far fewer comparisons.<br>If you use a non-stable algorithm, you might be introducing extra comparisons that could otherwise be avoided with a (less efficient) stable algorithm (e.g. input data is already sorted by time, and it needs to be sorted by something else followed by time). One algorithm could be vastly slower despite the same big O scaling.<br>If space complexity is an issue (which it often is for big data), then you&#39;ll benefit from an in-place algorithm, but if dealing with small datasets, doing them in-place might be slower. Unused memory doesn&#39;t speed up the CPU.<br><br>Always assuming the average complexity is just as naive as always assuming the best complexity (in which case bogosort wins hands down).<br>Also, small datasets aren&#39;t something that should be dismissed just because it&#39;s Google. One day, you&#39;ll be writing a function that will typically sort lists with ~10 million items, and another you&#39;ll be writing a function that will typically sort lists with ~100 items, but the latter might have to run for 100,000 small lists concurrently. Picking the wrong algorithm may easily set the company back $100k in server costs, at which point practical correctness is valued a lot more than theoretical.<br><br>tl;dr The interviewer could get their head out of their ass and maybe write some production code once in a while. <a href="http://www.youtube.com/results?search_query=%23doyouevencodebro">#doyouevencodebro</a> 

 	Replies: ['SimonDev', 'Well said!']

116: Mollyarty 
 Anyone ever tell you that you kinda sound like H. Jon Benjamin? 

 	Replies: ['SimonDev', 'hah yeah, he&#39;s got some great shows, so big compliment']

117: Adrian Haro 
 Was hopping to hear why the interview person disagree, I thought this was obvious that some algorithms do better at large ⚖️ 

 	Replies: []

118: your future self 
 ⭕❤ 

 	Replies: []

119: GameCyborg 
 also O(1) doesn&#39;t mean it&#39;s fast, just that the time it takes (or memory requires) is the same no matter the input size. 

 	Replies: []

120: Egwene Al'vere is cool 
 How do you compute big-O of non polynomial functions 

 	Replies: []

121: klfjoat 
 This is so true. I&#39;m just a humble sysadmin, but overhead matters once N gets large enough. Process a data set big enough (300 million records) and a 50ms constant response time from the API for each record adds up! Even if you parallelize it, the API-based processing can still take longer than linear batch processing on a single host. 

 	Replies: []

122: Ivan Wright 
 Knowing that people like that work at Google explains a lot of the problems with Google 

 	Replies: []

123: Ves Hallaes 
 All I understood was <a href="https://www.youtube.com/watch?v=gCzOhZ_LUps&amp;t=01m47s">01:47</a> 

 	Replies: []

124: Carey Pridgeon 
 It also depends on your problem and resources. During my doctoral research back in 2005 I had to keep the amount of memory used when processing a matrix constant regardless of the size of the matrix. This required sacrificing processing speed in favour of a working solution, since I simply didn&#39;t have the memory for a 6000x6000, matrix (36000000 objects representing genes) to be instantiated in memory simultaneously. Not ideal, and ungodly slow, but it worked perfectly every time. What I lost in efficiency I gained by not clogging up the system memory in my barely adequate cluster. Google engineers have the luxury of all the resources they need.<br>My solution would have irritated them, but it, plus another of my algorithms ended my Thesis defence in 45 minutes.<br><br>In 2008 they offered me a position based primarily on another algorithm I&#39;d designed for bookmark based recommendations. I was hugely unimpressed by the interview and turned them down, becoming a lecturer instead 

 	Replies: []

125: Поиск сути 
 That was a behavioral interview in disguise and you have passed it. 

 	Replies: []

126: Terje Mathisen 
 Having worked at both ends of the size scale for 40+ years I really feel for you! That interviewer simply didn&#39;t know what he was talking about.<br>The only way to really know is to benchmark &amp; profile your code while working with real (or at least realistic) input sizes. Personally I do care a lot about performance so I tend to keep thinking about a problem for sometimes several days just to be sure I understand enough about it, then I&#39;ll write my first implementation. During this stage I almost always realized that some of those initial ideas were simply wrong so I then write the second version.<br>Back to your examples, you can often make a hybrid solution where you switch from n*log n to n*n as soon as n drops below some cut-off value, simply because that will be faster.<br>A classic example is quicksort where, in my experience, the best approach is to switch at somewhere in the 4-8 range, or you can put the cutoff at 3 and simply use branchless code to sort the 2 or 3 items remaining. It is however far more important to always recurse into the smaller partition first and then handle the larger part with tail recursion, i.e. looping. 

 	Replies: []

127: Side egg unnecessary 
 BIG O, IN ACTION!! 

 	Replies: []

128: Espressonator 
 At <a href="https://www.youtube.com/watch?v=gCzOhZ_LUps&amp;t=2m19s">2:19</a> or thereabouts, you get the wrong quantifier on the multiplier M; you didn’t call it M at that point, but it’s M in the Wikipedia article that you referenced and showed. Your words were “for any constant“, but it should be “for some constant”. 

 	Replies: []

129: Anthony Zeedyk 
 All of that stuff about x &gt; x_0 is encapsulated by explaining how Big O is a function that describes the upper bound of an algorithm&#39;s growth function as the input size scales upward. Big O says nothing about how functions perform with small input sizes, and including that feels like a digression unless you state simply &quot;Big O says nothing about how functions perform with small input sizes.&quot; Big O is all about the scaling behavior of an algorithm. In practice, it says almost nothing about the absolute complexity of a program. 

 	Replies: []

130: arkie87 
 It doesnt feel right that any algorithm can be classified technically as the worst performant one e.g. O(N!). It should require that the O() is the smallest O that still fulfills the requirement.<br><br>It is surprising a google employee doesnt know big O notation only applies to large N. I once had an argument with a student about discretization schemes when solving PDEs, as the student thought that a higher order scheme is always more accurate, when in a similar fashion to this, it is only more accurate for fine meshes (large N). At coarse meshes, the error can be larger. <br><br>big O notation only describes the ratio of the computation time (or memory) that an algorithm takes between two points. It does not describe the relative ratio between different algorithms, except when N-&gt;infinity. 

 	Replies: []

131: Thad 
 <a href="https://www.youtube.com/watch?v=gCzOhZ_LUps&amp;t=3m18s">3:18</a>, x^5 (said politely!) 

 	Replies: []

132: Noah Tell 
 Well technically if you put the criteria for N to be bound by a constant value, the algorithm runs in O(1). Now you are allowed to optimize. 

 	Replies: []

133: endrawes 
 That guy at Google is an idiot 

 	Replies: []

134: Netik77 
 Spoiler: the interviewer was actually a google intern 

 	Replies: []

135: T 
 My estimation was wrong about 1 thing.<br><br>I did see the:<br>&#39;big-O describes better <b>at larger inputs</b> &#39;-issue coming.<br>And how that was a lesson that was going to be a big part on this video.<br><br>However I also had the &#39;assumption of competency @ google hiring practices&#39;<br>Therefore assumed (when I clicked on the video), that you would be the one making the mistake, not the other way around. 

 	Replies: []

136: Gnome 
 Google Drive is the perfect example that you can have the smartest people on the planet and still build horrible, buggy and slow Software.<br><br>Takes 3 times longer than Dropbox.<br>Keeps restarting.<br>Syncs only one file at a time.<br>Uses only one thread.<br>Deletes the last 6 digits of file timestamps so that your file will always have mismatch timestamps, Lol.<br>Has a horrible minimalistic UI.<br>Do I have to go on?<br>Google engineers are noobs that think they&#39;re so smart. Or they have horrible Management. 

 	Replies: ['SimonDev', 'I could rant about the reasons why Google&#39;s products are broken, it has a lot to do with what people are rewarded for doing.<br><br>In short, to get promoted, you need to have &quot;impact&quot;. Easiest way to have impact is to launch a feature, go for promo, then quickly transfer off the team before the feature breaks down. Rinse and repeat.']

137: Coda Highland 
 I took the Big-O questions out of my interviews for reasons like this. It&#39;s a trivia question. It doesn&#39;t tell me anything about how good the candidate is at coming up with good solutions or at implementing robust code. 

 	Replies: ['SimonDev', 'Good call. It&#39;s hard enough to get any sort of good signal about a candidate&#39;s abilities.']

138: Neehize 
 Big-O notation is about complexity, not performance. For a large input, complexity will have a great impact on performance. So I agree that Big-O tells nothing for a small input.<br>However from a Software Engineering perspective, I would say that mentioning micro-optimiations in a question related to Big-O is irrelevant. Big-O is important on any piece of code that deals with potentially large input while micro-optimisations are only useful in very specific cases where you are working on critical code. 

 	Replies: ['Neehize', '@SimonDev Oh I see, that makes sense in that context. Keep up the good content!', 'SimonDev', 'Possibly, but here&#39;s the larger context, since I thought this was enough for the video. I&#39;m a gamedev with a resume full of optimization work, in an interview where each interviewer is asking my about my optimization work, and now in a discussion relating performance and optimization. So I feel that yes, in this case bringing it up is warranted. We&#39;re literally already talking about it.']

139: ふくめい 
 The fun thing about O notation is that if n is a constant then everything is O(1). 

 	Replies: []

140: Mein guter Name 
 Feom the title of the video I was hoping for some new insights on big O (teasing us with &quot;what it ACTUALLY means&quot;). <br>I was a quite disappointed, nothing new, nothing special, just very standard what you learn in beginnners classes. Well-explained though. <br>To me the video was more about an introduction to big O, and hey there are people working for big companies that are quite convinced of them but lack some basic understanding. Maybe a surprise when doing a first interview at a company like google, but shouldn&#39;t be a surprise after some years of working experience 

 	Replies: ['SimonDev', 'I didn&#39;t think it was a surprise either, but I&#39;ve run into a bunch of engineers who didn&#39;t know this, my interviewer included. All of them at Google, weirdly enough.']

141: Claudio Brogliato 
 Yep. There&#39;re tons of video where fastest algorithms turned out not to be the best bigO ones in specific domains and with specific constraints. 

 	Replies: []

142: distro logic 
 Very good conclusion. Also good to note that the complexity of an algorithm may depend on the structure of the input. For example, a sorting algorithm may be much faster on inputs which are already partially ordered. In the end you need to think very carefully about what kinds of inputs you expect and what the expected average case is and that is what you need to optimize for. 

 	Replies: ['SimonDev', 'As always, profiler is king.']

143: Luke R. 
 What an asshole interviewer! It’s a shame you didn’t have a little more time to explain on a whiteboard or something. Thank goodness you still got the job. 

 	Replies: []

144: Jacob Zimmerman 
 Should jave asked the interviewer about Python&#39;s default sorting algorithm, then. It&#39;s called timsort, which uses the &quot;slower&quot; algorithms on smaller collection sizes and &quot;faster&quot; ones on big collections. I forget which ones, specifically, but it supports your point. 

 	Replies: []

145: Daniel Astillero 
 Very well made video 

 	Replies: []

146: Chris Solace 
 Makes sense. Maybe in large searches that Google handles it matters, but in smaller scenarios like characters in a game, linear may be better. 

 	Replies: []

147: InkDevil 
 Thanks for the video! I never understood Big-O properly or so i thought. I basically had the same understanding as the one you presented but my lectures somehow convinced me otherwise and i ended up VERY confused. 

 	Replies: []

148: Andrew Esh 
 The interviewer was probably deliberately disagreeing with you to see how you handle the frustration of another engineer telling you that your are wrong, when in fact, they are wrong. He was trying to pick a fight, to see if you&#39;d stick up for yourself. It&#39;s the Kobayashi Maru test, in a microcosm. It&#39;s not about being right, it&#39;s about how you handle confrontation. Given your description, I&#39;d say you passed the test. 

 	Replies: ['SimonDev', 'Hah, I&#39;d love to believe that, and totally would have a long time ago. Having worked at Google now, I can safetly say that these people absolutely are not playing 4D chess. I&#39;ve been through interviewer training, and conducted god knows how many myself. It was an interviewer who has probably never been checked out by anybody else, giving terrible interviews. Or if he was in fact, deliberately being hostile, that&#39;s so off the rails that under better circumstances, he&#39;d get reported to a manager.<br><br>I&#39;ll take the lesson on knowing when to just &quot;shut up&quot; though, heh.']

149: mkdir 
 Was going to say, that in general, could just use theta instead of O for average run time- but you clarified at <a href="https://www.youtube.com/watch?v=gCzOhZ_LUps&amp;t=6m29s">6:29</a>. <br>But I think generally, Software Engineers are only really concerned with worst case- and avoiding that upper bound function (depending on input ofc) . 

 	Replies: []

150: JDC2890 
 People need to understand that Big-O establishes an upper bound on stuff like time taken, not the ACTUAL time taken. For small input sizes it might be an exercise in futility. 

 	Replies: []

151: Vitulus 
 Surprised you didn’t mention galactic algorithms — they have better time complexity but have so many hidden constants that the algorithm is infeasible. 

 	Replies: []

152: Strateeg 
 Damn this is even something I know, as a non-CS student who learned this in his 3rd programming course. 

 	Replies: ['SimonDev', 'I feel like it should be common knowledge, but it seemed to catch a few people off guard over my career so I thought maybe not?']

153: MADMAN 
 The Big-O notation only helps when you know your expected problem size. 

 	Replies: []

154: R L 
 As a mathematician, idiots like these make my blood boil. Either accept that you don&#39;t know what you&#39;re talking about because you don&#39;t know enough about that area of math, or learn it before making claims. This is stuff you learn in the first two semesters at university if you learn math. Unless you are wanting to use extremely large (or, on the opposite side extremely small) numbers, O(f(x)) tells you very little about how fast the algorithm runs. Optimising O(f(x)) is an especially bad idea since that is only useful should you use extremely large numbers and hugely detrimental for small ones 

 	Replies: []

155: DeusExAstra 
 I also work in game development, and my philosophy for these types of things is to first consider the size of the data sets the algorithm will be working with, then consider things like Big O, and lastly test at least the top 2 choices I have to verify what I expect to happen.  Because of what you point out in this video, often times a &quot;better&quot; algorithm will be inferior in your particular use case.  But, it&#39;s hard to know for sure until you test it. 

 	Replies: ['Julian', '@SimonDev I feel like all of this is ties in nicely with Amdahl&#39;s law - &quot;the overall performance improvement gained by optimizing a single part of a system is limited by the fraction of time that the improved part is actually used&quot;. We can sit back and say &quot;wow; nice optimization here!&quot; or &quot;ah yes, the asymptotic runtime is much better here&quot;, but without thinking of the context of the optimization or algorithm they can be exercises in mental gymnastics instead of providing a true benefit to the product. <br><br>Always refreshing to see videos and comments like the above. I&#39;ve been focusing on how to retool how I conduct interviews the last couple years (game industry) and I think it&#39;s important to keep these types of wisdom in mind.', 'SimonDev', 'Definitely, profiler always has final say']

156: Mattia Giambirtone 
 That Google engineer is a colossal moron and probably never heard about galactic algorithms. Heck, even NP complete problems like the TSP can be solved faster with a brute force approach as opposed to a more clever exact algorithm or even an approximation for a sufficiently small n. 

 	Replies: []

157: Nian's Channel 
 Holly shit, well done. 

 	Replies: []

158: Nima 
 The example you showed here is one case where the O(n) outperforms the O(log n) algorithm  for pretty large examples.  I think up to about 10 MB of data, thanks to caching and SIMD, linear search usually outperforms binary search.  In a lot of my own time at Google, I noticed people writing slow code by using the asymptotically-fastest algorithm and ignoring this. 

 	Replies: []

159: Smiggy Balls 
 &quot;steaming pile of math notation&quot; lol 

 	Replies: []

160: mrKreuzfeld 
 Easy to prove with example (pseudovode):<br><br>function f1(x) {sys.sleep(10^1000); return ×[1] }<br><br>function f2(×) { return sum(x) }<br><br>f1 is O(1), f2 is O(n). f2 is always  faster, since f1 will wait until the heat death death the universe 

 	Replies: ['SimonDev', 'But... the first one is O(1), it&#39;ll run faster!<br><br>/sarcasm']

161: Alexander 
 Thanks for the video. To be honest, i was just here to refresh my knowledge for upcomming interviews, but eventually realized something new. 

 	Replies: []

162: Yolo Swaggins 
 People often slip through the cracks at these large orgs, like your interviewer here. Glad the system worked and you didn&#39;t have to have him as a direct colleague in the end. 

 	Replies: ['SimonDev', 'I&#39;ve done the interview training at Google, and conducted who knows how many interviews myself. This was totally off the rails.', 'Vulcwen', 'A smart interviewer might still do this to test how you&#39;d deal with nonsense.']

163: Caliburn Leaf 
 During your story about the interview, all I could think of was &quot;the interviewer needs to hear an example to understand.&quot; I find providing absurd but simple examples can really help illustrate a point. Like, suppose you have an O(n) algorithm, but for SOME REASON someone inserted a pointless sleep command for 1000 seconds, and you also have an O(n^2) algorithm that lacks the pointless sleep command. Until the O(n^2) algorithm&#39;s input becomes so large that its runtime exceeds 1000 seconds, it will be faster than the O(n) algorithm, despite being O(n^2) vs O(n). Thus proving lower order optimizations matter when dealing with small n. 

 	Replies: ['SimonDev', 'Yep, although I&#39;m unclear whether or not proving him definitively wrong like that would have cost me the job.']

164: xyzain _ 
 The guy at google was so obviously wrong, how did they get a job there? 

 	Replies: ['SimonDev', 'At Google, the hardest thing you&#39;ll ever do, is get into Google.']

165: Reynolds Kynaston 
 Bad interviewer 

 	Replies: []

166: Spellweaver 
 Technically, if you know your values are going to be within a certain limit (let&#39;s say, x&lt;1000000), every algorithm is O(1). 

 	Replies: []

167: garthbartin 
 I had a similar experience interviewing at Google. Interviewer asked a CSP problem disguised as a word problem. I got excited and mentioned CSPs. They didn&#39;t know what a CSP was and got noticably annoyed when my solution was the general approach to solving a CSP. They kept trying to nudge me towards the greedy solution that was presumably on their rubric....<br>Still got an offer and went on to conduct interviews myself. Google employees are bullied into conducting interviews so often times you get people doing a really half assed job and they might even be in an actively bad mood. 

 	Replies: ['SimonDev', 'I never minded interviewing much, and really tried hard to put on a good face/be warm to anybody interviewing. They&#39;re often stressed out, nervous, etc. and in reality, there&#39;s a lot on the line. But I can totally see why others would be annoyed with the process, takes hours out of your week, and you don&#39;t really get anything out of it.<br><br>There was a trick to get completely out of interviews, I forget the exact steps, my memories of Google are fading surprisingly fast, but in ghire (?) you could set a temporary period with 0 interviews, and you just extended that forever, there was no time limit. I knew a lot of people used that.']

168: yuehuang 
 Parallelism throws another layer of complexity.  Algorithm that can split the data set into chucks could be processed by different cores, but careful not to split too fine as the overhead could out weight the benefits. 

 	Replies: []

169: Josh 
 A bit late, but when I get into these arguments I like to fall back on this:<br><br>Runtime complexity of Algorithm 1: n + 2450 (due to some initial setup cost)<br>Runtime complexity of Algorithm 2: n^2<br><br>Anyone could tell you that as n approaches infinity, A1 is a far bettter algorithm. But for small n (in this case n &lt;50), A2 actually performs better. 

 	Replies: []

170: Jason Scott 
 This is why interviews should have multiple interviewers. 

 	Replies: []

171: Robert Wilson III 
 Google sucks 😂 

 	Replies: ['Robert Wilson III', 'But this video makes a really good point, after all computers are strictly finite, discrete and rational.  Big O makes no sense for many tasks.  This is where the Tilde comes into play.']

172: ds 
 You&#39;re definitely correct on the smaller datasets executing faster on less efficient algorithms but from what I learned in uni, Big-O measures the worst-time complexity. In short, it is on the assumption that the dataset went to infinity.  Also for bigger corporations, although they may benefit from the less efficient algorithms at the start for faster processing, in the long term and for scalability it would be better to go with the worst-case results. Hence questions are asked as such. Still appreciate your videos and it was great review of the things I had forgotten, thank you! 

 	Replies: ['SimonDev', 'Yeah, we actually talked about Google scale, and then game optimization scale, and the differences therein. This is a key part of understanding, at game and micro scales, you know exactly how &quot;many&quot; things there are. And if you&#39;re dealing on the order of milliseconds or less, things like cache misses start to get really important. The only takeaway I had was that, sometimes you need to profile and not make assumptions.<br><br>Remember that I was interviewing, at the time, as a game developer, who had done a lot of optimization work, my interviewers knew this, I discussed it with each of them, and eventually I went on to be hired specifically for an optimization team.']

173: Mark J 
 Geez, hard to believe that the hiring engineer at google couldn&#39;t comprehend that haha.  Like you said, depending on the engineer, Big O can refer to the Typical or worst case performance.  They often won&#39;t even consider the best case that you can guarantee with known input domain. 

 	Replies: []

174: Guilherme Feyh 
 You were technically right in the interview but i stand with the other guy. There is no such thing like &quot;O(N) is faster than O(log N) for smaller inputs&quot; in general. You could say one particular O(N) algorithm is faster than one particular O(log N) algorithm with a particular small input. But whats the point? This is a statement on specific algorithms that does not hold true in general. Anyway, good thing that you got the job despite of that. 

 	Replies: ['SimonDev', 'Right, but that isn&#39;t what I said. Maybe the video wasn&#39;t clear, but to clarify, I was talking in the context of game optimization and micro optimization. I specifically called out the difference between at &quot;scale&quot; and at micro scales and small values of n.<br><br>I&#39;m a game developer who&#39;s done a lot of optimization work, was being interviewed by people who knew that and asked questions specifically related to that, and was eventually picked out by a director in a major org for a nascent optimization team.<br><br>And this was an interview, whose sole purpose is to probe a candidate&#39;s depth of knowledge, so showing a nuanced understanding of the topic is important.']

175: LePonyOfHappiness 
 Seems google doesn&#39;t understand big O notation, you&#39;ll be successful with or without them, that interviewer doesn&#39;t understand shit. 

 	Replies: []

176: cx24venezuela 
 Yes, you was right about sometimes o(n) is fastee than o(log n). But here is the thing , You really need to Focus on doing things, and not over optimize. Make a perfect algorith is taking a suboptimal time to be implemented 

 	Replies: ['SimonDev', 'Yep, don&#39;t disagree at all. An interview&#39;s literally &quot;only&quot; purpose though is to probe a candidate&#39;s depth of knowledge, so showing nuanced understanding of a subject is good, isn&#39;t it?']

177: Not a Translations Channel 
 If I was sure of my answer I would have just told that interviewer to fuck off. 

 	Replies: ['SimonDev', 'Heh, I&#39;m not willing to do that. Google paid something like $200k starting, and around $500k for senior engineers, and I will literally never see that dude again. Just a couple years of that pays for my kids&#39; entire futures.<br><br>Personally, I don&#39;t see the difference between letting him win that battle and any other time you have to step aside during work for an obnoxious lead/manager or whoever else.']

178: Devin Walters 
 Great explanation 

 	Replies: []

179: Friendly Xerrol 
 did you ever get a chance to follow up with that engineer after getting the job? 

 	Replies: ['SimonDev', 'Nah, it&#39;s a huge company, the offer came quite a while after the interviews (Google moves SLOWLY), and I&#39;d have to remember their full name. You meet probably a dozen people the day of the interview, and you&#39;re so hyper focused on the stress of the situation that doing things like remembering names isn&#39;t a priority.']

180: Bernd Eckenfels 
 Such interviews can really be anraging, and it’s not representative for the interviewer org or the interviewee (unless you snap then you might lose) 

 	Replies: ['SimonDev', 'Yeah, no sense in failing the interview over pride.']

181: Luuk de Ruijter 
 What an absolute clown of an interviewer 

 	Replies: []

182: Alex Loskutov 
 It&#39;s called asymptotic complexity for a reason. 

 	Replies: []

183: Vok250 
 This is super important in cloud computing where you might saw split your computer across thousands of tiny virtual instances running on small data sets. Like a classic serverless on Lambda solution. 

 	Replies: []

184: Micky Kannalles 
 Great Video! I&#39;m a ce student and I failed my &quot;languages and complexities class&quot; once and really did a lot of studying on the second try. There are also quite a few more interesting things to this topic. <br><br>It feels so awkward that the engineer tried to put you down on something like this, especially because it&#39;s not super difficult and something students learn pretty early on. <br><br>Sry for the bad interview but honestly that gives me some confidence that these people are also just humans and not some sort of godlike, super smart, higher entity. 

 	Replies: ['SimonDev', 'I ended up at Google for ~7 years, senior engineer leading teams. Don&#39;t buy into the myth that they&#39;re all superhuman. They&#39;re not in the slightest. There&#39;s some great people there, and some really mediocre ones (I count myself in this group). Honestly, a big problem at Google is just getting people to even do basic work in a reasonable timeframe. I was once asked by another lead to look into why one of their engineers had taken 3 weeks to just implement binary search.']

185: Nathan Gehman 
 As others have said, that interview story is really frustrating. It sounds like that Google engineer lacks the capability to understand meaning instead of what is technically correct. Yes, technically, big-O states that whatever ends up being better at infinity is the better option, but at my school, which isn&#39;t even a good school, we still learned with the graphs. And even though the professor taught big-O technically correct, it was still easy to see that for some specific use cases, big-O doesn&#39;t accurately describe what is actually faster. But when talking about it, you still need a way to describe the functions as linear and logarithmic, or whatever the 2 types of functions are. So since big-O is usually what is taught to describe that, it makes sense to continue using those words.<br><br>In other words, this Google engineer is the same type of person that won&#39;t understand the sentence &quot;Coffee are bad&quot;. Yeah, technically the sentence should be &quot;Coffee is bad&quot; but &quot;is&quot; and &quot;are&quot; are 2 different forms of the same word so just use your fucking brain (note: I don&#39;t actually dislike coffee please don&#39;t kill me). Or he won&#39;t understand a sentence when &quot;you&#39;re&quot; is used when &quot;your&quot; is the correct word. Yeah, it might be slightly annoying. <i>Fucking deal with it.</i> 

 	Replies: ['SimonDev', 'I&#39;ve really having trouble moving past your hatred of coffee. We can&#39;t be friends.']

186: Miguel G 
 have you ever been told you sound like bob from bob&#39;s burgers? 

 	Replies: ['SimonDev', 'Indeed I have heard that']

187: Georg Plaz 
 I have seen some sort algorithms that check the array size and then branch to a different sorting algorithm based on that. can&#39;t remember where, maybe some standard library java? 🤔 

 	Replies: ['SimonDev', 'Yep, many do that for this very reason.']

188: Roland Hutchinson 
 Technically correct is the best kind of correct. 

 	Replies: ['SimonDev', '<b>insert Futurama image</b>']

189: Duncan McPherson 
 I have to admit that your interviewer&#39;s perspective kind of makes me lose a lot of respect for google engineers. Knowing how large your design space is, is critical to finding out how much time to spend optimizing which algorithms. And not being able to back down and admit when you&#39;re wrong as an interviewer just makes you look incompetent and insecure. Obviously, they&#39;re working at Google, they must know what they&#39;re doing, but it&#39;s definitely not a good look. 

 	Replies: ['SimonDev', 'There&#39;s this myth that the engineers there are amazing, next-level. The truth is that, getting into Google is the single hardest thing you&#39;ll ever do at Google. Once you&#39;re in, many people coast, and there&#39;s a reason the term &quot;rest and vest&quot; exists.']

190: Jon Wallace 
 Experienced engineers know the quirks of big O and it sounds like the Google guy was just a dick.  I use radix sort probably more than qsort because it’s way way faster for my datasets.  Things like that matter especially in low level optimizations in assembly.  Profiling trumps theory every time, and estimating actual performance is very difficult when you have tons of threads and cores.<br><br>In fact, Im like 95% sure most implementations of qsort actually check the size of input and quicksort for in most cases but the last few recursions on smaller sets switch to a radix. 

 	Replies: []

191: Corey Hartman 
 If someone talks to you like this, it&#39;s not a team you want to work for. 

 	Replies: ['SimonDev', 'You&#39;re almost guaranteed not to end up on the same team. The process basically throws a bunch of random engineers at you, who submit their feedback privately to an internal tool, and another committee reviews the feedback to make decisions.']

192: Gordon Chin 
 That sort of bureaucratic buffoonery is why Twitter runs like hot garbage, loading the same page multiple times etc. 

 	Replies: ['SimonDev', 'Beauracracy &amp; politics is a problem at pretty much every big company. I remember a senior engineer at Google telling me that they probably got more done in a morning at their previous job than they did in a month at Google. People erect fences, guard their turf, etc. It&#39;s just how it is.']

193: Time Traveler 6048 
 Big-O notation always confused me when I was first introduced to it. I wasn&#39;t taught a formal definition right away, but just the informal one where it just means that f looks like some constant multiple of g. What confused me about it was the smaller values. In an Analysis course I took some years later, I was finally taught a proper definition, and was introduced to big-theta, little-o, and more. And the teacher made it extremely clear that big-O (or any-O) notation is meaningless without the phrase &quot;as x tends to a&quot; (where a can be any number including infinity). If that phrase is not included, then we could say the function f(x)=x^2 is both O(x^2) and O(1). The first is true when x tends to infinity, the second when x tends to 0. 

 	Replies: []

194: fr89k 
 I also know a software engineer who optimizes almost solely on Big-O. However, I work on embedded systems with limited storing and computing capabilities. The amount of data I can receive and process is very limited. I need an algorithm that uses my small CPU very efficiently on these few data points. I don&#39;t need an algorithm which could potentially work on millions or billions of data points in a data center application. But even for such big applications, my feeling is that some software engineers too often look solely at the algorithm and not enough to the data. Maybe the data is sorted in a specific way already due to some external restrictions? This definitely changes the real-life behavior of the whole thing. Also, it&#39;s important to look at requirements. Do I want to have a guaranteed maximum processing time? Or is the throughput more important? (aka average processing should be fast). For some tasks this might actually result in the same algorithm, but for other tasks it might not. Also: How accurate does the result actually have to be? I know that software engineers like to think in deterministic ways, but if working on real-life data and when we want to create practical results, sometimes it might be more important to be accurate to a few percent accuracy instead of being fully accurate - but the processing time can be vastly smaller on some tasks. 

 	Replies: []

195: finmat95 
 Wow....the worst part is you were NOT wrong. Big-O is  a notation that describes the limiting behavior of a function when the argument tends towards infinity, it doesn&#39;t say ANYTHING for small or limited values. 

 	Replies: ['finmat95', '@video_hosting_account Correct.', 'video_hosting_account', 'Maybe the interviewer was evaluating his reaction to being faced with someone who is being aggressively wrong. SimonDev passed the test by first trying to explain, not becoming angry, and dropping the subject gracefully. He did get the job offer in the end.']

196: TeXoN 
 Just have a look at Timsort. This is faster than Mergesort, because it starts by sorting groups of five with Insertionsort and then merging them together like Mergesort.<br>For lists smaller than six Insertionsort is faster than Mergesort. 

 	Replies: []

197: Михайло Сєльський 
 Array search caveat: before binary search you need to sort that array o_0))) 

 	Replies: []

198: anthony cannet 
 That interviewer is dumb af... I would&#39;ve started drawing graphs and shit to prove my points. Like how you do in this video, obviously as you get to larger values of X we can clearly see by graphing those functions that logN is better than N, but in this region here, where f(x)=x is less than f(x)=log(x), that&#39;s not the case. You can clearly see that the worst case time for linear search is lower in these small cases compared to the logarithmic growth despite the fact that logarithmic is better than linear in larger cases. For a videogame, there is generally a cap on things like number of entities due to computational performance limits, meaning if our linear growth function is always lower than the logarithmic growth funtion for any case less than or equal to our maximum number of entities, using the &quot;slower&quot; function is actually optimal. With the cap in place we&#39;ll never have enough entities for the logarithmic function to out perform the linear one. <br><br>You definitely shouldve talked to someone about that interviewer... 

 	Replies: []

199: RipleySawzen 
 I would have <b>LITERALLY</b> asked that interviewer if he was stupid. I would have then gone to his boss and explained why his interviewer needs to be fired. 

 	Replies: ['SimonDev', 'That&#39;s unfortunately not how Google works. You do the interview, post your feedback through the internal tool, nobody else generally see&#39;s or comments on it. Nobody checks whether an interviewer is strong or weak, it&#39;s a bit of a luck of the draw.']

200: Krissam 
 That google interview story instantly took a huge bite out of my imposter syndrome, thanks. 

 	Replies: ['SimonDev', 'If you like that, I once was tasked with trying figure out why another engineer was taking 3 weeks to implement binary search.<br><br>There&#39;s no trick here, it&#39;s exactly as simple as it sounds.']

201: Sammy Gillespie 
 I knew where this was going from the title alone. It actually concerns me that so many people don&#39;t understand it, but I&#39;ve also had to explain it before. I gave the example of a custom function that sorts an array using quick sort, but before starting the function simply sleeps for 5 seconds. That function is still O(log n) - though that alone confuses people at first - yet it&#39;s clearly going to perform worse than even a bubble sort on small list. But start scaling up that input and suddenly that 5 second sleep becomes just a fraction of the sorting time, and O(log n) saves the day.<br><br>I&#39;ve seen similar with people who code using a variety of OO best practices, but because they don&#39;t fully understand why those things are done they end up creating a monstrosity of interconnected classes that can&#39;t be untangled. At the end of the day, real word experience really does matter a lot, but equally it seems to be easy to go years and years without ever being challenged on these points, particularly if people job hop.<br><br>Also, how amusing that YouTube just randomly suggested I watch this 2 year old video... Almost exactly 2 years old as well! 

 	Replies: ['Emil Riikonen', 'Wouldn&#39;t it be more likely to be challenged on these points since you run into more peers and thus have a higher chance of encountering someone who actually knows wtf they are doing?', 'SimonDev', 'It&#39;s super weird that Google suddenly picked this video up. I made it almost 2 years ago, but now suddenly YT is pushing it.']

202: Mo Atef 
 Software engineers who don&#39;t have the time to read up CS/math theory trying to cope with formal math will always be pretty funny. It&#39;s like with other types of engineers fudging physics or math theory and angering all the physicists and mathematicians. 

 	Replies: []

203: magfal 
 This is why I test my performance sensitive solutions with different sizes of problems to see if the performance overhead scaling is linear, sub-linear or super-linear. 

 	Replies: []

204: YeYaTeTeTe 
 Your mistake in the interview was talking about small numbers when using Big-O notation. Everyone knows that for small numbers you use little-o notation. And at the end of the interview you use cheeri-o notation.  The start of the interview is worst though, because you have to use hell-o notation. 

 	Replies: ['SimonDev', 'This is gold']

205: Awwastor 
 I think the simplest way to explain to somebody how much constants matter in performance analysis to somebody is to show them two implementations of an algorithm, e.g. linear and binary search and then insert something like a wait(Duration::from_seconds(3600)) in the “faster version”, then ask them about the complexity of the algorithm again (it didn’t change), before benchmarking one against the other (you probably don’t want wait until the binary search which waits an hour for each split completes though) 

 	Replies: ['Gabriel Fonseca', 'Alternatively, you can make the wait time scale linearly to show how an algorithm scales in general (for some tests it&#39;s difficult to see a difference)']

206: Mikael Isaksson 
 Sounds like that Google engineer didn&#39;t understand. But I have met people like that many times. Very certain about things because they have been taught it but have no real world experience to the contrary, so they have never thought more deeply about it. 

 	Replies: ['SimonDev', 'Being wrong is fine, everyone is wrong occasionally. Just like, don&#39;t be actively hostile towards being corrected.']

207: Rik Schaaf 
 Either the interviewer was playing devil&#39;s advocate and you had to give a clear example of what you meant (just like you did in this video) and the interviewer was applying pushback, to show how you might not always have an easy time convincing the other party, unless you are clear with your explanation.<br>That, or the interviewer was just a dick who didn&#39;t know big-O well enough themselves. 

 	Replies: ['SimonDev', 'To be clear, I worked at Google for 7 years, and did interviews the entire time. There was no recommendations for a &quot;apply pushback&quot; approach to interview, and pretty much everyone I knew made efforts to make candidates comfortable, and at ease, to get the best info out of them.<br><br>There were, however, tonnes of people with ego problems there. More so than any other place I&#39;ve worked.']

208: KDSBest GameDev 
 Great Video. I usually always ask the compiler, if I know something like an upper bound. I create a test scenario for e.g. 1000 entities and then profile it. Sometimes a more complex algorighmus might squeez the last 5-10% performance, but if it already runs on speed with 200 fps. Then I like to keep the simpler one with the other one at hand when we need it.<br><br>I worked as a consultant for years and have seen people optimize ridiculous things. It wasn&#39;t search but let&#39;s say it is search for analogy. In search a junior developed something like a bubble sort. Works, but super slow. After a client complained about the performance senior wanted to optimize it, because it is slow. Me also senior wanted to profile first. I was allowed to profile, but he replaced the bubblesort with quicksort. After profiling his change gafe a performance boost of 0.01%. Because the arrays being sorted were 50 elements long or so. Profiler pointed us to really really bad things.<br><br>ALWAYS use a profiler or in C# a stopwatch (Start at the start of a method, stop at the end and write it to a log file.). This way you find what is slow and then you check the why.<br><br>Also as an interviewer I try to never say directly no you are wrong to a interviewee. Always keep in mind, that someone might know more than you about the topic. Even if I believed that you were wrong with the Big-O thing. I would have said something like &quot;I&#39;m not sure if what you said is correctly. I think differently, but let&#39;s keep it at that. I might be wrong and you might be right.&quot;. Then I have time to educate myself after the interview. Also I&#39;m old and learned that later in life :D 

 	Replies: []

209: Olly Wood 
 The next video to watch after this is any documentation on <b>Quake III fast approximate inverse square root</b> 

 	Replies: ['SimonDev', 'I remember coming across that when I was first learning to program, back when the source was first released. I spent forever deciphering it, would make an interesting video and trip down memory lane.']

210: 47Mortuus 
 Yap, the <i>obvious</i> solution is to sort the list first and now get a completely useless index. 

 	Replies: []

211: Freddy Koehlmann 
 Its also important to point out that when working with asymptotic bounds they are describing a mathematical behaviour and even when they do provide an initial cost (n) before the algorithm becomes faster the practical implementation almost always has a higher initial cost before it becomes faster. 

 	Replies: ['Dan Nguyen', 'Just like manufacturing processes.']

212: Mr. Kodirovsshik 
 This was the most basic introduction to Big-O I&#39;ve seen in my life<br>Where&#39;s the title-promised &quot;ACTUAL&quot; meaning???<br>Thanks for wasting 10 minutes of my life 

 	Replies: ['Mr. Kodirovsshik', '@SimonDev Yeah, you have a fair point here<br>At least I should not have been this aggressive and instead put my point more constructively, I&#39;m sorry', 'SimonDev', 'I guess there&#39;s ways of looking at it. Be angry you didn&#39;t learn something new. Be happy you already knew seemingly more than this experienced engineer did.']

213: Ed Munns 
 As a Civil engineer currently working on a highway bridge I have found this dismissing of coefficients and scalars so liberating! We are Big O(n)! 

 	Replies: []

214: Xcoder112 
 As the end of the video tells you, just never rely on big-O alone. I did that once, choosing a hashtable for a situation where data is frequently looked up but rarely added or removed, because it is O(1) (it&#39;s a little worse for collisions, but the table would never be loaded by more than 50%, so collisions would be very rare). I didn&#39;t even consider other solutions. Years later, just for fun, I wanted to test how much slower a sorted list would be at lookup, after all it is O(log2 n), only to find out that it beat the hashtable by a long shot; it was much faster. So I calculated at what point the hash table would take over, and it turns out I have to have over 300 entries before the hashtable gets faster (I benchmarked that and the benchmark confirmed it). The thing is: Due to other technical limitations, it was impossible to ever have more than 256 entries, and even numbers over 50 would be pretty rare. Why was the hashtable so slow? Because of the hashing. In the time it took to hash the data for a search, a binary search of a sorted list would have found the entry long ago. However, a good hashing is indispensable, because with a bad hashing there are many collisions and the hashtable then becomes even slower. 

 	Replies: ['Tim de Jong', 'Red-Black trees or similar binary search will be faster than hash tables at smaller number or elements yes. In my experience, in C++ the unordered_map will be slower than the map depending in the context. Could still be faster after thousands of elements.', 'Purplox', '@Mo Atef IMO software engineering not being a &#39;real&#39; engineering discipline (read: Not relying on physical systems, not being primarily done by engineers, not requiring an engineering background, etc.) implies that it is just an application of computer science in an ordered, process - driven, formal manner. If that is your definition of software engineering, and mine is, then there is no disciplinary boundary. Software engineering would be akin to laboratory work in the same way experimentation would be for a physicist or chemist.', 'Purplox', '@Mo Atef I mean, the alternative is that you rely on gut instincts and misinformation. It&#39;s better to use big O responsibly then not to use it at all just because of some pseudo disciplinary boundary.', 'Mo Atef', 'You should never rely on big-O alone PROVIDED you are a software engineer or applying asymptotic analysis to algorithms you write to be used. Asymptotic analysis is applied to computer science from a theoretical perspective, it is used in the theoretical study of algorithmics and data structures. It wasn&#39;t ever meant to have any claim on the practicality or non-practicality of specific implementation of algorithms. Algorithmics is a theoretical/mathematical subject, and asymptotic notation certainly has its place there. The problem occurs when say software engineers (understandably) want to use the same general ideas of &quot;faster&quot; and &quot;slower&quot; implementations, but slowly fudge the meaning of big-O so much that it is no longer accurate. And then claim they understand big-O notation.']

215: bløtz 
 Beautiful explain. Just spent 4 weeks in lectures learning what was beautifully explained in 10 mins 

 	Replies: []

216: A form of matter 
 So the interviewer was just wrong? Seems like maybe they shouldn&#39;t have that person conducting interviews. Or working at Google. 

 	Replies: []

217: jeanalpha2401 
 As a good example for this google guy : Simple multiplication algorithms. Karatsuba is great for large numbers but for small numbers you take the usual route. Even worse : Schönhage–Strassen, an algorithm  that offer an excellent complexity but only outperform Karatsuba when the number are over 10 000 digits at least ! 

 	Replies: []

218: Dixaba 
 My favorite example of &quot;O(n) is a meaningless metric when n is small&quot;. Key observations:<br>1) multiplying 2 numbers (as we learn in school) takes O(n^2) steps;<br>2) multiplying 2 numbers is pretty much the same as calculating a convolution of those 2 numbers (after splitting them into 2 lists of digits);<br>3) you can calculate convolution using Fourier transform (takes O(n^2) steps) + n times single-digit(-ish) multiplication (takes O(n) because we multiply single digits which is O(1) lookup) + inverse Fourier transform (takes O(n^2) steps);<br>4) ... but you can use fast Fourier transform instead to reduce complexity from O(n^2) to O(n log n) steps;<br>5) considering facts 1-4, using FFT you can multiply 2 numbers using O(n log n) + O(n) + O(n log n) == O(n log n) steps, which is faster than using school multiplication algorithm.<br>All 5 facts are mathematically provable, nothing wrong there.<br><br>... but for sOmE WeIrD rEaSoN, computers don&#39;t use FFT to multiply numbers, at least until numbers are bonkers huge. Hmm, probably software and hardware engineers just don&#39;t know about this neat trick 

 	Replies: ['Ahm Asaduzzaman', 'Booth&#39;s algorithm is a technique for performing multiplication of signed integers in binary notation. It was developed by Andrew Donald Booth in 1951 and is still widely used in modern processors.', 'Anony Mousse', 'I use FFT to enjoy my spare time. Best Final Fantasy game.', 'DragonEdge10', 'Even without a practical example, it&#39;s so easy to visualise just by pulling up the basic Big O comparison graphs. There&#39;s quite literally like 3 different &quot;bad&quot; runtimes that have better performance under like 10-25 items. That Google interviewer was just on a power trip.', 'Scott Hebert', '@bloos A somewhat more specialized case is the Simplex algorithm for solving Linear Programs.  In all but degenerate cases, its performance is optimal.  However, because of those degenerate cases, the actual Big-O for the algorithm is NP.  There is a P-time algorithm, the elliptical algorithm, but it&#39;s so slow for any &#39;real&#39; purpose that no one, AFAIK, uses it.', 'bloos', 'There are many different other examples. Almost every standard algorithm is suboptimal from a theoretic asymptotical standpoint, but optimal for realistic inputs. Matrix multiplication is another example']

219: MangoTek 
 I&#39;m here for the giant robot fights. I think I&#39;m lost. 

 	Replies: ['SimonDev', 'Come, sit down, grab a drink and enjoy some computer science']

220: Bloom HD 
 Today I learned you don&#39;t have to be smart at all to work at Google as an engineer! You just have to agree and pump their egos :D 

 	Replies: ['Bloom HD', '@SimonDev very true. love your vids', 'SimonDev', 'Isn&#39;t that a basic rule of interacting with other human beings in general?']

221: PierceXLR8 
 Wow. You&#39;re still active in comments. I&#39;m impressed 

 	Replies: []

222: Axim Vidya 
 so in a way, the engineer who was interviewing you was the one who actually failed the interview. 

 	Replies: ['SimonDev', 'It&#39;d be neat if it worked that way. &quot;Sorry, you made a mistake, we&#39;re going to have to switch seats, I am now the interviewer.&quot;']

223: Tommy Productions 
 cool video but why do you say effedex instead of eff of ex 

 	Replies: []

224: Polysixx 
 If I were in your situation, after I got the job, I would’ve found his desk and left my algorithms textbook open to the section on Big Omega/Big Theta notation with a note to the effect of “cuz it seems like you need this more than me.” 

 	Replies: ['SimonDev', 'I was rejected from that office (possibly because of that interview), so never got a chance heh. Not that I&#39;d even have remembered his name.']

225: jake lee 
 big o is only one part of algorithm analysis, and will give you the idea at large values for n, but an important thing to understand is there are other things to take a look at besides big o class, such as algorithm properties: for sorts it is important to know if it is in-place or stable, for say hash functions it is going to be more important to know how fast they run rather than their big o class (bench marking), and for small lists a big o n^2 algorithm can beat a big o n*log(n) algorithm take for instance insertion sort, there are versions of insertion sort that will beat quick sort for lists smaller than 45 or 50 long. 

 	Replies: []

226: Ram Kumar 
 Basically domain is 👑😎 <br>Books and Equations only go so far 

 	Replies: ['SimonDev', 'Actually understanding those books and equations is also useful']

227: KaizerKilborn 
 &quot;If I got anything wrong, please let me know...(long pause) Politely.&quot; That cracked me up. Great info. Thanks for making the video! 

 	Replies: ['SimonDev', 'Gotta remind people sometimes heh']

228: Mailbox 
 O(TREE(n)) 

 	Replies: []

229: columbus8myhw 
 Wait, what was the error in what you were saying in the interview? Sounded like you were right! 

 	Replies: ['columbus8myhw', '@SimonDev Woww', 'SimonDev', 'There wasn&#39;t one, I was right, the interviewer was wrong, and I had to be careful about how I corrected him since he was so hostile about it heh']

230: Alejandro Quinche 
 Even in one of my most scrappiest classes we discussed a lot why merge sort or others neede a minimum size to be faster, and like 3 of the most used sorts do a hibrid of some n² sorts with the classic reccursion not just to be different. I wonder what branch that engineer worked on... 

 	Replies: ['SimonDev', 'No idea, guessing it wasn&#39;t optimization']

231: Тимофей Черников 
 I don&#39;t understand. It seems you were totally correct during interview. Why did google engineer say you&#39;re wrong? 

 	Replies: ['SimonDev', '@Тимофей Черников I worked there for 7 years, the hardest part about Google is passing the interview heh<br><br>After that, the work itself is incredibly undemanding', 'Тимофей Черников', '@SimonDev wow, I guess it&#39;s easier to get a job at Google than I thought!', 'SimonDev', 'Because he only had a basic understanding of Big-O, and I&#39;m guessing some ego problems.']

232: Jon Time 
 I had a quite similar interview with the big G many years ago, making almost the same observation and was met with the same disbelief.  I wasn&#39;t hired, but I had a quite long and productive career anyway.  This was a really clear explanation, and yes sometimes the details and specifics of the constants can&#39;t be swept under the big O carpet. 

 	Replies: []

233: yonoseespanol 
 I woulda just asked the interviewer to evaluate y=5x and y=x**2 with x = 2 

 	Replies: []

234: Adam Myers 
 I think, like scientism and the reification of science, this is an effect of reifying the mathematics, assuming that because the math “says” something that approaches a result close to what we intuitively mean by a certain word or phrase, then it must mean the same as that intuition, rather than being contingent on a host of assumptions.<br><br>For example, when I say that, given the interval between 0 and 1, that the probability that a random number chosen is a rational is zero, I am relying an a very particular use of the term “chosen”. In reality, any number that a human would ever choose would be a computable number, and most likely would be a rational number (if not the integer 0 or 1). Exactly how one describes what is actually being said matters a great deal on those circumstances.<br><br>Most things are nuanced, that is how life is. 

 	Replies: []

235: Ralph Parker 
 If you know the break even point, you can test for it.    Sometimes below the break even point, the difference isn&#39;t worth the test time. In those cases the lost efficiency isn&#39;t re-capturable. So the default would be  technique &gt; N break even.   After this, I&#39;m going to have to get the weeds off my ankles.  Thanks, good video. 

 	Replies: []

236: T33K3SS3LCH3N 
 I&#39;m glad my profs taught this correctly. &quot;Simple&quot; algorithms (like O(n²) for sorting) for few elements, and &quot;advanced&quot; ones for big ones (typically O(n log n)).<br><br>There may be a better term for it, but I consodsr the added cost for advanced algorithms with better O-scaling &quot;overhead&quot;. They usually achieve their performance either with an elaborate setup that is performed before the iteration, or with a significantly higher effort per iteration. Like how quicksort may perform a median of 3 and does a lot more writes per step than something like selection sort.<br><br>I was taught to consider around 100 elements the cut-off at which we should expect advanced sorting algorithms to perform better, although it of course depends on the particular algo and implementation. 

 	Replies: ['SimonDev', 'Like anything, profile']

237: NutronStar45 
 i didn&#39;t think google interviewers can be this stupid 

 	Replies: []

238: Jeffris (Suspicious Manifold) 
 There&#39;s a great opportunity for clickbait right there: &quot;What Big Data doesn&#39;t want you to know about Big-O!&quot; 😉 

 	Replies: ['SimonDev', 'Hmm maybe I should switch the title...']

239: pendragon 
 That Google interview is an idiot. This is basic stuff, taught in any first course on algorithms. It&#39;s called asymptotic performance for a reason. 

 	Replies: []

240: Dabbo Pabblo 
 Not just in a game, googles servers like any other companies of their size scale horizontally meaning any of their computers are only ever processing below a certain number of events every moment before a new server gets spun up automatically for new requests to overflow to, Not to mention the entirety of video processing at YouTube happens on embedded processors specifically designed only for the purpose of muxing video rather than code running on an operating system which as a result constrains their resource usage by an INSANEE amount and means quantity over quality of those video muxers is applied, making algorithms that perform better linearly potentially better in some of their cases 

 	Replies: []

241: Jazzling 
 epic video!!!!!!!!!!!!!!!!!!!!!!!!! 

 	Replies: []

242: Daniel W. R. Hart 
 That interviewer is an imposter 

 	Replies: []

243: ReEngineer 
 when something like this happened to me I thought it wasn&#39;t about code at all. Thought it was  some kind of a  behavioural test. 

 	Replies: ['SimonDev', 'I was an engineer at Google for many years, never heard of these kind of behavioural tests. Occam&#39;s Razor, guy was just full of himself.']

244: James R T 
 Don&#39;t feel bad for standing your ground if it is the truth!<br><br>This concept is also applicable even in non-contrived real-life applications. Sometimes, your input to a particular problem will never be larger than a googol or something. Hence, an algorithm with worse theoretical time complexity can still be better 99.99% of the time compared to an algorithm with better theoretical time complexity. The keyword here is &quot;theoretical&quot;.<br><br>At other times, you have to make a tradeoff between space and time that might make the algorithm with better theoretical time complexity unfeasible to be implemented. Examples that come to mind include hybrid sort algorithms, BVH for ray tracing, and even integer multiplication. For example, using the Schönhage–Strassen algorithm is way too expensive for everyday integer multiplication.<br><br>It&#39;s not always so black-and-white as &quot;O(logN) is ALWAYS better than O(N) and that&#39;s that!&quot;. The whole point of software engineering is to be able to weigh these different options and tradeoffs and select the appropriate solution for that particular application, guided by testing, profiling, benchmarking, etc. Sometimes, even measurements can lie (though not often), hence the importance of code review, design/architectural discussions, etc. For example, embedded systems might not have the luxury of space (or even power!) to perform heavily recursive algorithms or algorithms that require large data structures such as trees or graphs. Hence, selecting the slightly slower algorithm might be better for that specific case. 

 	Replies: ['SimonDev', 'Well said!']

245: Pupper Gump 
 I remember watching some video about how O(n) == O(2n), and they never explained what that meant. Bugged me for a few minutes before I came up with the answer. 

 	Replies: []

246: Dominik K - KFP🐔 
 I&#39;m really glad that you explain the difference and fallacies for Big O notation for small numbers too! <br>I&#39;ve been bitten by this misconception of co-workers too, especially when CPU cache-friendly algorithms with worse Big O notation are just way faster for certain use cases 

 	Replies: []

247: Marcus Aurelius 
 I’ve been doing code for 24 years in large corporations and smaller companies. And these little videos warm my heart. Nothing new for me here, but clarity and simplicity of explanations is brilliant. Thank you. 

 	Replies: ['Tekbox', 'Yeah I never fully understood Big-O notation except that it&#39;s supposed to show whats faster but thats about it and school didn&#39;t do a good job explaining it to me', 'SimonDev', '~20 here']

248: karoshi2 
 Have seen similar things, usually with NP completeness. Like colleagues insisting that you cannot implement say a traveling salesman algo because that&#39;s NP complete, although you&#39;re sure to have at most five elements. And when you show them the implementation and runtime, you&#39;re the guy who &quot;proved all uni wrong&quot; and you&#39;re the &quot;coding deity&quot;, etc etc.<br>Or they don&#39;t look at your implementation and you&#39;re a liar and trickster from then on and they won&#39;t listen to anything you bring up anymore.<br>-_-<br>Neither outcome is helpful. 

 	Replies: ['Planarity Theory', '@Martin O&#39;Donnell factoring is not known to be NP-hard (and our best guess is that it isn&#39;t)', "Martin O'Donnell", 'The TSP general case isn&#39;t NP-Complete, it&#39;s NP-Hard. Factorization is NP-Complete', 'Jeffris (Suspicious Manifold)', 'That little detail can get overlooked: if you know the size of your input is constant and the thing you&#39;re implementing won&#39;t be used elsewhere on a different scale, it&#39;s O(1) and the Big-O thing becomes kinda moot.', 'SimonDev', 'People are weirdly dogmatic.']

249: The PineApple 
 I make sure all my algorithms run in O(n!) time so I have free time to do stuff while the program runs 

 	Replies: ['SimonDev', 'That is genius']

250: esapilves 
 To comment the end of the video: if you know there&#39;s at tops 1000 entities, then x&lt;=1000 and values above that are irrelevant by the definition of Big-O: &quot;if there EXISTS a value where f(x)&gt;g(x) blabla&quot;, but values for x&gt;1000 do not exists if you choose not to define the function when x&gt;1000. This does stretch the intuition of Big-O, but I don&#39;t see it being wholly incorrect. 

 	Replies: []

251: Jacob Palazzetti 
 this is so easy to understand, even though i was lost halfway through it all came together at the end 

 	Replies: []

252: Markus Miller 
 I&#39;m actually shocked that this Google engineer did not know that... 

 	Replies: ['Markus Miller', '@SimonDev Well, at least you got the job anyway. Some interviews are quite silly anyway. While doing my PhD I had a couple of interviews and most of them only had the purpose to see me jump through hoops. And some were even lying to me and my supervisor. At the same time they complain about not finding suitable employees. Crazy world and it&#39;s just getting crazier 😅', 'SimonDev', 'I&#39;m generally ok with people not knowing things, as long as they&#39;re not super difficult about being corrected. We&#39;re all learning, regardless of seniority. There are holes in my knowledge. But being in a position where you&#39;re deciding if someone gets a life changing job, and being so full of yourself, that kind of sucks. I still got the job, luckily there are more interviews during the day where you can make up lost ground.']

253: ss l 
 Google has 150,000 employees. They are paid well but that doesn&#39;t mean some random engineer there is going to be smart. 20 years ago sure, not now. A company can&#39;t get that big without hiring a lot of mediocre people. It&#39;s not like you were interviewing to be a research assistant to a CalTech professor. 

 	Replies: ['SimonDev', 'Agreed, often these kind of tests only gauge how well you interview.<br><br>Not that it matters, but this actually happened 12 years ago, and the engineer in question had been there since the mid-late 2000&#39;s, I believe. Also, 150k employees, but not engineers. There&#39;s 27k (as of writing this comment), with a crazy number of those coming in the last few years.']

254: foobars 
 Is there any chance that that last interaction was just them testing how you deal with conflict? Seeing how you would deal with somebody telling you that you are wrong even though you are actaully correct. I heard that they sometimes do tests like that, but maybe it was incorrect info? 

 	Replies: ['arkie87', '@SimonDev When i first saw the title of your video, I thought you were going to say that you mistakenly said that O(N) is always faster than O(N^2), not realizing it doesnt apply to small N. I was surprised it was the interviewer who didnt know that!', 'SimonDev', 'I worked at Google for 7 years. I&#39;ve done countless interviews. I&#39;ve never done that, nor read feedback from someone who did, no spoke to anybody who planned to test for that, nor was trained in interview training to look for that.<br><br>What I HAVE run into at Google is an absolute abundance of people with a raging ego, who saw getting in as validation.']

255: mohamed sabir 
 Actualy, you outsmarted the google guy but he will never note that anyway great explanation dude 

 	Replies: ['SimonDev', 'That&#39;s ok, I still made it in.']

256: FlareGunDebate 
 Programmers and engineers can get touchy about Big-O. I also once mentioned to a senior dev that O notation is accurate as n approaches infinity and they got pretty emotional about it. Probably because I have no professional experience? So I backed up and pointed out that even if an algorithm is O(n) and n was equal to 1 million if our target platform is powerful (like the average cellphone) it will still execute quickly. But that backfired because he never considered that Big-O was being applied to a hypothetical machine and argued that O notation was &quot;just math&quot;. I wasn&#39;t in a job interview but things still got awkward. 

 	Replies: ['insidetrip101', '@SimonDev I think its because if you read a book about algorighms, generally they admit that O notation applies to a hypothetical machine with special properties for operations...<br>but that&#39;s not the world we live in--which is what you&#39;re trying to point out--so it ends up looking like a contradiction. Who cares what O notation says at that point, if you&#39;re looking for a solutionf or a specialized case, then O notation is pointless anyway.', 'Luiz', '@DragonEdge10 You can get by with just knowing to read graphs, then you can compare the algorithms after a search on wikipedia to know what the algorithm&#39;s O is.<br><br>They teach it like you were Knuth writing your own algorithms for sorting, but you are going to use one that already exists.<br><br>And no one will be calculating the O for an entire program, you just use a performance profiler and look for hot paths to optimize, O-notation is useless for that.', 'Luiz', '@DragonEdge10 There&#39;s no mathematical intricacies, its just stupid instruction counting and graph plotting.<br>No one needs an actual formal proof that some algorithm is O-n-squared or something.', 'DragonEdge10', '@Luiz I always just teach that you don&#39;t need to understand any of the mathematical intricacies of Big O, nor do you even technically need to understand it at all to become successful at programming, but it&#39;s extremely helpful to understand what general concepts mean and how to use them to decide what algorithm to use for specific usecases. Even for those that don&#39;t understand Big O formally, if they&#39;re successful they probably have an innate understanding of that fundamental concept even without the formal knowledge.', 'dale116dot7', '@LuizSometimes instruction counting and little optimizations are necessary. If n is small, then the order of the algorithm may not matter, and that was the point of the video. The video was spot-on. I write embedded controller code (automotive ECU code) with a fixed memory size (recursion isn’t a great idea), fixed and fairly slow processor speed (100 MHz, limited by ambient temperature) and my code often does searches on sorted data with n &lt; 16, always. Linear search is faster than binary search. I also play a trick, I search from top down, and engine speed is a common search I need to do. Now, the trick is that engine speed and interrupt loading tend to offset each other, so in fact I effectively get better than O(0) performance out of the search in the real world. As RPM climbs, the searches require fewer steps but there are more processor interrupts from the crankshaft sensor signals, so the actual run time of the algorithm shortens. In the actual system, interrupt loading swamps the search algorithm complexity and the processor becomes more heavily loaded as engine speed increases. But a “more efficient” search algorithm in terms of O will perform worse.']

257: Strider 
 I remember being made fun of back at the university, when I said array lengths should be taken into consideration when picking the sorting algorithm 

 	Replies: ['Jason Kaler', 'I lost marks once for an answer that was technically correct but not in the text book.<br>I even brought in documentation published by intel that proved my point but it was just discarded.']

258: J T 
 I love the story about Google. Sure, their workers are brilliant minds, but they also make mistakes, and this is just one of the many stories I hear. We really need to stop idolizing MANGA workers like people do celebrities. 

 	Replies: ['SimonDev', 'There&#39;s definitely some smart people there, but working at FAANG doesn&#39;t immediately make you a genius. It just means that you passed a difficult interview once.']

259: Andrew900460 
 Also a nice story of when somone becomes so &quot;lost in the books&quot; that they can&#39;t actually think for themselves. They treat all their formal education like it came straight from the Bible and you can&#39;t refute it in any way. Not a very creative, wise, or engineering mindset, I would say. 

 	Replies: ['SimonDev', 'Definitely, with a touch of &quot;I&#39;m at Google and you&#39;re not, so I&#39;m smarter than you&quot; mentality.']

260: Colin Marcus 
 The graphs were nice but often misleading... 

 	Replies: []

261: siquod 
 Don&#39;t write f(x) = O(g(c)). The correct notation is f(x) ∈ O(g(x)) because complexity classes are sets and I have no idea how the wrong one could ever become popular. 

 	Replies: []

262: Gamer Steve 
 Are you sure that guy was an engineer? Quicksort, one of the most used sorting algorithms is a prime example, since its worst-case performance is O(n^2), but on average it&#39;s O(n log n), and faster than Merge sort, which is O(n log n) in the worst case.     <br>The point all my programming teachers always made was that you have to <b>benchmark</b> to actually know the performance of your algorithm. Hardware details and input characteristics can make a huge difference.   <br>And you also need to know your priorities. Sometimes the average case doesn&#39;t matter at all, if you have a hard time/memory budget (e.g real-time programming like robotics and audio, or limited memory environments like embedded devices) 

 	Replies: ['Shiinon Dogewalker', 'that&#39;s still comparing O(n log n) with O(n log n), because if you hit worst case the quicksort will be very slow. A better example is that a common implementation of quick sort switches to an O(n^2) algorithm such as selection sort once the ranges gets small enough. If O(n log n) always was faster than O(n) you wouldn&#39;t be doing that and just keep using quicksort until it&#39;s fully sorted', 'SimonDev', 'Agreed, and yep, totally was an engineer. Internally, you have access to data like who interviewed you, their job and level, etc.']

263: M G 
 <a href="about:invalid#zCSafez"></a><a href="about:invalid#zCSafez"></a><a href="about:invalid#zCSafez"></a><a href="about:invalid#zCSafez"></a>❤❤❤ 

 	Replies: []

264: MegaSupernewbie 
 I feel like I am learning things all over again!!! 

 	Replies: []

265: Abhay Shiravanthe 
 This was by far the best explanation. Other videos just scare the F outta me. 

 	Replies: []

266: kerel 
 Beautiful. 

 	Replies: []

267: Bootstrapper 
 Amazing content! Thank you!! 

 	Replies: []

268: Furan 
 Imagine the interviewer going to more-knowledged colleagues saying &quot;and there was this guy saying that with smaller ns you may get better performance with a function in O(n) instead of one in O(log n) hahah&quot; and then a sudden silence follows with him realising that maybe he was wrong... lol 

 	Replies: []

269: Pedro Serpa 
 Well, thinking about the googler question is interesting<br>He wasn&#39;t wrong<br>Big O is about tendence to infinite, if there is no tendence, then its not Big O. So in a certain point of view he was right 

 	Replies: ['Pedro Serpa', '@SimonDev nice<br>That makes sense, thank you for replying it', 'SimonDev', 'I had brought up the context of micro optimizations, and how it&#39;s possible at small inputs for functions with technically worse time complexity to outperform ones with technically better time complexity. Again, at small inputs, not as they go towards infinity.<br><br>This is more of an advanced topic, but since he was quizzing me on Big-O, I thought it&#39;d be good to throw that in.<br><br>Big O says that a function f(x) is order g(x) if there exists a constant M and real value x_0 such that |f(x)| &lt;= M * g(x) for all x &gt;= x_0.<br><br>So yeah, he was totally wrong. But that in itself isn&#39;t all that interesting, people are wrong all the time. I know I am. What made it a memorable story was how badly he reacted to it.']

270: nicolas brown 
 thank for video❤️ 

 	Replies: []

271: OFfic3R1K 
 Your interviewer might&#39;ve never learned the definition of time complexity and it&#39;s hard to blame him. Computer science is not always fun and formal definitions are boring. It&#39;s much more fun to <i>just do things</i> and pick up other knowledge along the way. Sadly, then you might end up in a spot where your knowledge of, let&#39;s call it &quot;applied&quot; computer science, won&#39;t have enough nuance and you will get things wrong. It doesn&#39;t make you a bad programmer, but you have to be aware of your limitations. Of course, you can&#39;t rule out the personal aspect, getting schooled by a less experienced person can be a tough situation to handle for many people. 

 	Replies: ['SimonDev', 'That&#39;s totally ok, but then realistically you just shouldn&#39;t make it part of your interview. I was at Google for years, you choose your interview questions, nobody asks you to cover specific topics. He could have easily opted to cover other topics and called it a day, or discussed the topic but allowed for some nuanced discussion and been open to learning things. Google is however, home to more people with ego problems than any other place I&#39;ve worked.<br><br>I get schooled regularly by experienced people, you can&#39;t know everything, even in your own specialty.']

272: Nxte 
 Hey guys I really like the content and the math involved. Can anyone suggest a book that could teach the math necessary to computer science? Never had a university degree but I want to take my CS knowledge to world class levels. 

 	Replies: ['Nxte', '@SimonDev thank you so much man', 'SimonDev', 'Look for something covering trig &amp; linear algebra']

273: Min huang 
 Great stuff as always. Ever heard of interviews allowing for, say, appeals? I mean, there usually should be primitive checks on the process too, you wouldn&#39;t want someone stubborn like that who can&#39;t pick up on nuanced subjects at all to be responsible for the hired talent. Not that I spent too much time in the software industry, but getting to make a stand and defend the argument your interviewer rebuked seems like a pretty good heuristic if you&#39;re looking for competent workers. Either way, getting put down despite having done everything to spec is really disheartening. Only worth it if you get to redeem yourself in some form afterwards, but sometimes life is just about biting your tongue and knowing your audience, sadly. 

 	Replies: ['SimonDev', 'Appeals? No idea. I did pass the interview and ended up at Google for a long time, never heard of an appeals process for failing an interview.<br><br>The problem is that the pass/fail decision is pretty opaque to even the interviewers themselves. The way that it works (very hand-wavy) is that they write their feedback, and that&#39;s delivered to a hiring committee, that looks over the packet, feedback, scores, and ultimately makes the call. As an interviewee, I have no visibility into the process.<br><br>The biggest takeaway, for me, was reinforcing the lesson that you have to pick your battles :)']

274: Braeden Gaines 
 I have been enjoying your content. You have so much to teach about game design, software development, and mathematics. I appreciate it very much that you have posted on youtube for people to learn for free. I will be buying you a beer, friend! 

 	Replies: ['SimonDev', 'Awesome, thanks! Been a bit slow about new videos (doing a house reno, can see on my IG), but hoping to have a new one on Monday.']

275: CaffeineInjected 
 my brain hurts 

 	Replies: []

276: Mehdi Khody 
 I&#39;m a self-taught programmer and I just realized I don&#39;t know nothing about programming 🤣🤣. 

 	Replies: ['HaZe', 'Lol, most companies dont care about Big-O', 'Super Mario', 'Even the ones who went to University feel that way Fam.<br>😏']

277: Kochu Krissten 
 The day when the bananas and papayas join forces, they will take over the world and destroy it 

 	Replies: ['SimonDev', 'That&#39;s kinda scary']

278: Numbah9 
 Just found this channel through the JS MMO video. What an absolute gem. Thank you! Subbed with the bell on, but first I need to go back and watch all of these videos 

 	Replies: []

279: ou kid 
 Reminds me of a talk Johanathan blow gave where he explains how he was wrong arguing with the doom creators about using linear search instead of hash. <br><a href="https://m.youtube.com/watch?t=817&amp;v=JjDsP5n2kSM&amp;feature=youtu.be">https://m.youtube.com/watch?t=817&amp;v=JjDsP5n2kSM&amp;feature=youtu.be</a><br><br>Thanks for the upload, Simon. Always a pleasure to watch ur vids. 

 	Replies: ['SimonDev', 'Ooh neat, will watch, thanks!']

280: Frehnzi 
 Not sure if you know who this is or have gotten this before, but you remind me a lot of MadSeasonShow. Not only do you two talk very similarly but your mannerisms and methods of explanation are strikingly similar. His content is mostly all World of Warcraft related, and I think you like WoW too, since you did make that WoW clone in JS, so perhaps you two have even more in common. 

 	Replies: ['SimonDev', 'That&#39;s funny, heard a few people say that, looked at the channel but haven&#39;t watched any of their videos.']

281: Pi St 
 Awesome video! Thanks! 

 	Replies: []

282: TheHellishFrog 
 Surely - I have subscribed! 

 	Replies: []

283: Gabriel Zimmermann 
 you deserve 1m subscribers, will leave you a comment again when you reach them as you sure will. 

 	Replies: ['Gabriel Zimmermann', '@SimonDev thanks, it&#39;s a lot of work, it taught me to appreciate good quality videos. Totally underestimated how long it takes.', 'SimonDev', 'Thanks, I see you&#39;re also making vids, good luck on your channel too!']

284: Aqua 
 Your channel is so under rated. I’m a cs student and hated data structures and algorithms before watching your videos... now I can’t get enough. Thank you Simon. 

 	Replies: []

285: Joni Hanski 
 I always found big-o to be kind of a tool to do initial guess rather than any super accurate analysis. Like, you think of an algorithm, you can in your head calculate the O complexity related to inputs that you don&#39;t know how to constrain, and try to gauge if you think the complexity is needlessly large, and if you can do better.<br><br>For constrained inputs, O(1) is always an option. 

 	Replies: ['Seraphina Joyce', '@Travis Collier This is kind of the case in games in general as they usually do constrain the input sizes (often via settings). Thus what you really care about is whether the given profile can calculate frames in an acceptable period of time on the target consumer hardware. This of course being due to the fact games are very realtime in nature so ideally you want to cap the frame processing time somewhere. Probably in the range of 16ms on recommended hardware and 33ms on minimum hardware ideally as you have 16.66 ms at 60 fps and 33.33 ms at 30 fps to calculate and draw a frame. Any more and the game is likely to get uncomfortable to play although it depends somewhat on the game too with RTS games the limitation is often less about drawing frames in time as it is time dilation as entity counts grow but the game would still grow too glacial to be fun without such constraints.', 'Travis Collier', '@Sycration Xyrozalda Yes, it was (might still be) a common optimization for things like trig functions... Especially in old video games where &#39;good enough&#39; is the precision requirement. ;)', 'Sycration Xyrozalda', '@Travis Collier I remember reading about how some complex algorithm with only one float as an input found it actually faster to interpret the float data as an integer and look it up in a LUT than it was to do the math on the fly.', 'Shiinon Dogewalker', 'isn&#39;t O(1) the &#39;only&#39; option for constrained inputs?', 'Travis Collier', 'If the problem is finite, a lookup table is always theoretically possible ;)<br>Memory vs time optimization are different things.']

286: Karlsson 
 I really like these videos, thanks for making them! If you already have 2 implementations like in these examples, just benchmark the production code with production-realistic data to make sure. If you only have one implementation, try another implementation only if you see bottleneck there, or if you have a lot of spare time (Yeah, right...). 

 	Replies: []

287: Mehdi Ghanimifard 
 I was waiting for a concrete example. 

 	Replies: []

288: Willem M 
 Very practical example:  You can make Quicksort faster by switching to a different sort in the recursion step when the size is small enough (like, below 10).  I think it&#39;s called hybrid quick sort. 

 	Replies: ['Goffe', 'You can also randomise finding the pivot element in which case the chance that it&#39;ll be n^2 is..... really improbable.', 'Luiz', '@bloos yeah, bubble sort is ironically linear when the list is almost reverse sorted.<br><br>What I meant knowing it is reverse sorted happens when for example sorting a column in a grid.<br>You sort the same data in both directions.<br>In this case merge-sort is better than quicksort, even if you randomize the pivot.', 'bloos', '\u200b\u200b\u200b\u200b@Luiz haha. When you Know it is reverse sorted, you don&#39;t even need to sort it in the first place. The nasty cases usually are where the list is ALMOST reverse sorted except for some items that you don&#39;t know 😂<br><br>Actually the optimal solution in this case might be to flip the list and use bubble sort. The list is almost sorted and bubble sort is almost linear in this side case.', 'Gabriele Palma', '@Luiz The proper and most commonly used quick sort implementation uses a randomly chosen pivot, so that no input will deterministically lead to a worst case execution.<br><br>This is especially important in security for web facing applications where input can be chosen by attackers, making for example DDoS much easier to engineer if you skip that part.', 'Gabe Poudret', '@Luiz why not have a random pointer or the pointer be the median of the start, middle and end of the array?  Unless I&#39;m misunderstanding something here']

289: Euquila 
 that google engineer got <b>asymptaught</b> 

 	Replies: ['SimonDev', 'That is gold.']

290: N8 Programs 
 Thanks for this video! Really interesting to see how optimizations play out at smaller scales.<br><br>In a recent project of mine, I was considering using a spatial hash grid or some kind of tree structure rather than the naive O(n^2) algorithm. However, I ended up just trying the naive algo out, and since I didn&#39;t have too many agents, it performed well enough that I could still get 60 fps. Not sure if that directly relates to the topic of this video but definitely a cautionary experience with premature optimization. 

 	Replies: ['SimonDev', 'Great advice! A lot of programmers get caught up optimizing parts of the code that barely register on the profiler, wastes a lot of development time.']

291: J K 
 Just a minor thing, the last 20 seconds of the video throws up &quot;look at this next&quot; that blocks a bit of what you are showing. If it&#39;s not to hard work, for future videos, just add a 20 seconds epilog so the actual information in the video don&#39;t get blocked by youtube. Otherwise informative as always. 

 	Replies: ['SimonDev', 'Good point, I&#39;ll try to avoid that.']

292: Rob Rohan 
 This makes me happy that I never interviewed at Google :) 

 	Replies: ['SimonDev', 'It&#39;s not the worst experience, but it&#39;s already a stressful situation without an interviewer with an ego. It was worth it though, spending a large part of my career at Google was a great experience.']

293: Justin Scotty 
 Amazing video Simon! And loved that story from google, unfortunately there was that discussion, but also great to hear you still got a job there! Looking forward to your next video! 

 	Replies: []

294: Ambre P 
 passed 2 hours trying to explain that to my university teacher... ended playing dumb on the final exam to avoid a bad review... 

 	Replies: []

295: Rahul Kumar 
 What do u use to teach ( some kind of pen or digital whiteboard😅),<br>PLEASE tell i need to make my friend understand some concept and i wanna about it 

 	Replies: ['SimonDev', 'Just chrome canvas, nothing special.']

296: Honken 
 You know you&#39;re a <i>real</i> professional when you have temper tantrums over a technical discussion with a peer.<br><br>On a brighter note: Your content is amazing. It&#39;s very well polished, presented with a perfect balance between brevity and detail without losing neither educational quality nor entertainment value. Thank you for your hard work, I automatically click your vides when they show up on my feed. 

 	Replies: ['SimonDev', 'Hah!']

297: Sanbal_x 
 Hey, my question is did you use React in your JS game projects? 

 	Replies: ['SimonDev', 'Nope have never touched react before, know nothing about it.']

298: GuildOfCalamity 
 LOL, I feel like this video was just a round-a-bout way to call out that snob at Google. 

 	Replies: ['SimonDev', 'Hah, possibly a little... but it&#39;s been 10 years since this happened and Google was/is a huge place so it&#39;s unlikely you&#39;ll ever run into your interviewers again.<br><br>But I do like telling repeating this to people because it&#39;s a fun little story about not looking down on people and being a complete snob.']

299: Darko Vucetic 
 Great video. Tnx! 

 	Replies: []

300: Olaf van der Aart 
 I love how this is something they teach at Computer Science year 1 and still a Google employee tried to outsmart you on this, while you were absolutely right! Great video! 

 	Replies: ['Canal do youtube', 'I was really terrified right now, I was like, &quot;well, he is right, what the f..., does this google employee knows something I don&#39;t? f... I don&#39;t know shit&quot;.  Caught off guard', 'Richard Arriaga', 'I think I had an overview of this in AP Computer Science.  Crazy.  But then again I argued with my PI in grad school about how this reaction chamber was getting oxygen as embers literally formed inside a CVD setup.  Needless to say, I left without a degree.', 'Patrick', 'It’s not even computer science it’s just common math. Then again I learned about big O in aerospace math… yeah nvm that’s just applied CS, carry on.', 'Evan Friesen', 'Currently in my second CS course in first year and learning about big O as we speak lol', 'bloos', 'In my CS studies it actually was my second year (3rd semester). They taught a lot of maths and programming basics before']

301: Foz Tacticus 
 Yep, this matches my experience. The first time I encountered this, I was so puzzled why it was slower 

 	Replies: []

302: boudy hesham 
 great as always simon! 

 	Replies: []

303: Mozartenhimer 
 I bet that Google engineer got learnt from his coworkers after you pointed out that it&#39;s called asymptotic notation for a reason. 

 	Replies: ['Bill Kong', 'That google engineer looked it up anxiously that night and never mentioned this interview again.']

304: atila correia 
 That might explain why some internal sort implementations use Insertion Sort for small arrays and real Quick Sort implementation for big ones :) 

 	Replies: []

305: MrJloa 
 The interviewer was a junior dev?<br>Probly a Junior or just a book nerd, never made real-world apps. Not everyone building Facebook 

 	Replies: ['SimonDev', 'Nah, definitely not a junior. Not by a long shot.']

306: Thiago Alexsander Luiz 
 Cheers m8 

 	Replies: []

307: Joonas Kolostov 
 Cheers! Thanks for touching on that subject! Very useful with a clear statement! 

 	Replies: ['SimonDev', 'Glad it was useful!']

308: Space Flight 
 Your videos are really eductional. This one taught me something I didn&#39;t know. 

 	Replies: []

309: Henrix98 
 For shit&#39;n&#39;giggles, 1000*log(n) is faster than 0.001*n after 1.66*10^7 iterations/entities/whatever (and about in between 0&lt;n&lt;1 

 	Replies: ['SimonDev', 'Hah, didn&#39;t actually check the exact crossover point, thanks!']

310: Waffle1434 
 That interview story really gets my blood boiling. I can&#39;t help but feel like there&#39;s systemic misinformation about optimization, people often deduce performance based on assumptions rather than observations. Implementation details are everything when it comes to performance, its the reason an optimized brute force algorithm can easily out perform a poorly implemented &quot;smart&quot; algorithm, while simultaneously being cleaner. Not that smart algorithms are bad, but you should actually verify optimization rather than assume it must be better. 

 	Replies: ['calmbbaer', '@SimonDev - What do you think was going on inside his head at the moment, his rationale?  I mean, how can you even interview for this without knowing the very, very basics of it?  All I can think of is Spinal Tap and the befuddled, &quot;These go to eleven.&quot;', 'Peter Johnson', 'I remember one case in the early 2000s where I was sorting through a <b>very</b> small list of numbers (a mostly sorted list, max 32 entries, used as part of a game for some reason I can&#39;t remember anymore), and spent quite some time figuring out why my naive bubble sort algorithm that I wrote on a whim was beating out everything in the standard library.<br>The answer was cache behavior and branch prediction.', 'Mike Propp', 'This reminds me of a Mythbusters episode about UPS trucks never making a left turn, because in the long game they save more time/fuel by only making right turns. Even if in this one instance a left turn would be more efficient than three rights, overall, the three right turns win (per the myth).<br><br>My guess is, because Google (and YouTube) have problems on scale, it makes sense for them to always assume large-scale data when designing algorithms. It seems the engineer you were interviewing with couldn&#39;t take his blinders off to see the real world around him. I&#39;d call seeing the world that way wearing &quot;Google Glass&quot; but that name has already been trademarked <br> :)', 'Dennis', '\u200b@bloos My guess would be that the interviewer looked it up after the interview, or someone else reviewed the interview notes and realized you were right.', 'VancomycinB', '\u200b@ZeddBloaxigan I feel like he could have drawn the graphs on the board, exactly like he did in this video. Nerves probably stopped him.']

311: Ezequiel Garrido 
 Great job as always Simon. 

 	Replies: []

312: Brian Haddad 
 Big O notation is a lot like spelling diarrhea to me. I don&#39;t ever remember enough details to feel confident doing it, and if it&#39;s gotten to the point where I need to do it I&#39;m probably in a pretty crappy place anyway. If I had to do it more often I&#39;d probably be pretty good at it. 

 	Replies: ['Brian Haddad', '@SimonDev just because I don&#39;t spell it out often doesn&#39;t mean I don&#39;t get diarrhea often. 😉', 'SimonDev', 'Good point, I was thinking of times where I might have sat around and had some sort of discussion. Times where you follow code around to a bunch of nested loops, that&#39;s not uncommon. So maybe using it in that sense, definitely way more often.', 'Ingvar Mattsson', '@SimonDev Heh, I have used it informally about monthly since leaving the G, and probably informally weekly at the G. But, I was also working on large-ish systems, where N was usually never less than 10**7. To be fair, in at least one case it was &quot;does the O(poly) approximation give sufficiently good bounds guarantees that we don&#39;t have to go for O(n!)?&quot; (note that in this specific case, n would normally be in the 40-50 range). And by informally, I mean things like &quot;hm, this latency here is much larger (well, usually spikier) than it really should be, it lives in that code over there, can I see a loop in a loop, because that feels like it should be O(n log n) and it behaves as if it&#39;s O(n**2)&quot;. And then, with the change in place and a representative data set, look at the new metrics. Because no matter what your O&#39;s say, measure and measure again.', 'SimonDev', 'I&#39;ve used it informally every few years, and in a serious way twice. When I learned it in University, and the Google interview.']

313: Christopher Karlsson 
 Thanks for pointing me in in the direction of what math I should be learning. Always been coding, never had an interest for math. Strange combo but what can you do. 

 	Replies: ['David H', 'I hated maths in school. I love it now but I struggle endlessly with proper maths notations. It&#39;s so much easier when people describe maths through code.', 'SimonDev', 'That&#39;s pretty normal, see a lot of coders who don&#39;t have a mathy/computer science background. Had a bunch who were my bosses, so didn&#39;t hurt their careers much heh.']

314: Pushy 
 So essentially, when in an interview, just play dumb if your interviewer is not receptive to learning. 

 	Replies: ['I. Wyrd', 'Maybe not play dumb, but definitely don&#39;t answer the question <b>more</b> than you need to.  Interview is less about showing off you&#39;re smart, and a lot more about convincing them you&#39;ll totally be a team player who&#39;s agreeable and easy to work with.  Swallow all pride.', 'Alex', 'When you gaze into the abyss, the abyss also gazes into you. If your interviewer is being confidently wrong, and even demeaning, that&#39;s a red flag for the company. If they fail your interview over it, then you <b>definitely</b> don&#39;t want to work there.', 'Lynn Trisinscius', 'No, you stand firm when you know what you&#39;re talking about and end the interview. Would be a horrible place to work if they have someone who doesn&#39;t even know what they&#39;re talking about doing interviews. Clearly they want conformity, not truth.', 'Bilbo Swaggins', '@TheCablebill None as far as I know. There&#39;s tons of islands that aren&#39;t actually part of any continent', 'TheCablebill', '@Bilbo Swaggins what continent contains Hawai&#39;i?']

315: Eddie Ye 
 So what did the interviewer mean by you don’t understand the Big-O? <br>If x doesn’t scale into infinity, do we not use the Big-O? That area where the ignored constant is still ignored even on small scale calculation? 

 	Replies: ['SimonDev', 'Pretty much what Pushy said. The guy had an ego.', 'Pushy', 'Seems like the interviewer just had a superiority complex and didn&#39;t like being corrected.']

316: dempa3 
 Very interesting and accessible for a person like me who has learned programming from YouTube tutorials and has a background in something completely different. It&#39;d be very interesting to see more videos on the subject of efficient/performant code, and then to see you apply these principles in practice on something like JavaScript game code that you wrote. 

 	Replies: []

317: Avi Chetlin 
 One of the best explanations of time complexity i&#39;ve seen, thank you! 

 	Replies: []

318: leomelki 
 Super interesting video, happy to see your channel growing fast haha! 

 	Replies: []

319: Poiq 
 Great video! What do you use for drawing, software? 

 	Replies: ['SimonDev', 'Chrome canvas, nothing special. Lots of redrawing, since I suck at drawing. Lots of editing.']

320: YO MAN 
 Thanks for the video, pretty cool stuff 

 	Replies: []

321: Tuomas Koivistoinen 
 Very useful 

 	Replies: []

322: Shapeless 
 First thing I thought when you said one way would be better than other was &quot;How about small numbers?&quot; 

 	Replies: ['SimonDev', 'Yep! Did you watch the last 4 minutes of the video? I covered exactly that 😉', 'SimonDev', 'Hah, good catch!']

323: Agent_A0x007 
 Starting A DSA Series? 

 	Replies: []

324: _creare_ 
 What the.... lol this is some complex sutff 

 	Replies: []

325: Dylan H 
 I appreciate the Office Space reference 😉 great video as always. 

 	Replies: []

326: Nate Wec 
 I&#39;m considering this studying, as this is tangentially related to what I&#39;m supposed to be doing right now :) 

 	Replies: []

327: Alkeryn 
 they also very often tend to not realize that even a O(n²) algorithm will tend to be faster on actual hardware than even O(log n) types algorithm for small values of N ( could be up to millions) because of stuff like cache optimisation, memory locality branch predictions, and other kinds of optimizations.<br><br>they also tend to ignore the time a single iteration take.<br>yes O(log n) will have less iteration than O(n^2) but if a single iteration is thousands of time slower you might prefer the O(n^2) one 

 	Replies: ['Dragonax', 'TIL iterations aren&#39;t equal', 'Alkeryn', '@John K n can be up to 100k or even a million and still be faster with n^2 than log n in some cases.', 'John K', 'idk, for most applications it would seem that a modest constant is going to be acceptable, but you want to avoid worst-case scenarios as well as avoiding scaling issues. I&#39;d probably choose logn over n^2 every time, cause if n is small enough to where n^2 is faster, it&#39;s irrelevant anyways. Maybe if you were doing some embedded thing it would be different', 'Arseny Pogosov', '1e6^2/log(1e6) ~ 1e11. You are clearly insane.', 'Sergeeeek', '@Oblivion to go into a bit more detail on this: cpus never load just one value from ram, they load &quot;cache lines&quot; worth of data at once. The size of a cache line is dependent on the cpu, but usually afaik it&#39;s 64 bytes. <br><br>For example let&#39;s say you want to load a single 32 bit number from memory. Instead of loading just 4 bytes, the cpu will load an additional 60 bytes after it as well. The assumption the cpu is making is that you&#39;ll most likely will want to load some memory right next to your first number so it overfetches. <br><br>Knowing that you can optimize your code significantly if you lay out your data linearly in arrays. <br><br>Another insight from this is that the less memory you&#39;re using, the faster your code will be. Let&#39;s say you have game objects of size 64 bytes. Even if you lay them all out linearly in memory you will still get a cache miss on each iteration (not necessarily because the cpu might pre load more cache lines, but still). If instead you can somehow compress your object to be only 16 bytes then iterating through the array will be many times faster. <br><br>With these two things in mind you can see how some dumb bruteforce algorithms that use memory properly are way faster than smart algorithms that have bad memory access patterns']

