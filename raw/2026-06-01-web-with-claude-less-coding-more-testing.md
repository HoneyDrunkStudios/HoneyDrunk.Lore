---
source: "https://henrikwarne.com/2026/05/31/with-claude-less-coding-more-testing/"
title: "With Claude: Less Coding, More Testing"
author: "Henrik Warne"
date_published: "2026-05-31"
date_clipped: "2026-06-01"
category: "Developer Tooling & AI Coding"
source_type: "web"
---

# With Claude: Less Coding, More Testing

Source: https://henrikwarne.com/2026/05/31/with-claude-less-coding-more-testing/

With Claude: Less Coding, More Testing | Henrik Warne's blog 
Henrik Warne's blog 
Thoughts on programming… 
Skip to content 
Home About 
← In Praise of –dry-run 
With Claude: Less Coding, More Testing 
Posted on May 31, 2026 | Leave a comment 
Having used Claude Code for a few months now, I have noticed how software development has changed for me. I write a lot less code, but I spend more time understanding and testing the code Claude has written. The proportions have changed, but it still feels like software development.
I also use Claude to better understand existing code that I didn’t develop. On balance, using an LLM coding agent is very positive for me. It speeds up many parts of development, without losing the joy of creating software.
Fundamentals 
I am far from the bleeding edge when it comes to using agents. I still look at the code, even if Claude wrote it. I sometimes edit it. I believe it is important to understand how the system I am developing works. This includes understanding it on many different levels, from architecture down to implementation details. Ultimately, a system is made of an enormous amounts of details. 
When I add a feature, I want to know and understand how the system is changed by my addition. I may forget some of the details later, but I want to have understood them all at least once. I know many people feel that the specification given to the agent should be enough, and that developers no longer need to care about the details. But so far, I am sticking with understanding the details too. This is partly because with my name on the change, I want to be able to vouch for it. It is also because there are so many details in an implementation that can’t be captured in a short specification. Many of those details will affect the behavior of the solution. It reminds me of the essay Reality Has a Surprising Amount of Detail by John Salvatier.
Coding 
These days, I typically start a new feature by asking Claude if the description in the ticket is correct, and if so, I am asking for a suggested solution. I avoid steering Claude to a given solution, even if I have one in mind. Perhaps there are better ways of doing it that I haven’t thought about. I also don’t want Claude to just go along with whatever I suggest.
When the code is written, I will read through it to understand it. There is often a back and forth with Claude: what does this part do? why is this here? how does that work? There can be both big and small things to change during this process.
It is great not having to write boiler plate code myself, or finding the right syntax, or figuring out the correct way of using an API. It is like going straight to the logic of the change.
Testing 
I have always wanted to convince myself that the change I am putting my name to will work. Apart from seeing the main logic working with unit tests and integration tests, it means making sure every line of code in the change has been executed, seeing that the log messages look good in context, observing the whole system when using the feature, and so on,
With Claude, it is so easy to get tests set up. Before, it could take a lot of work to create the right environment for tests to be feasible. Apart from automatic tests, I like to do some exploratory tests too. With Claude, it is easy to ask for some temporary local changes to facilitate this. For example, if some processing is only done at midnight, I can get patches to make my local test system execute that logic one minute after starting, instead of having to wait for midnight.
Understanding 
AI is not an excuse for not learning. On the contrary, learning is still important, not least in order to be able to judge the answers the AI is giving. Perhaps the most surprising benefit of using Claude has been how useful it has been in exploring the existing code base.
I regularly ask Claude to explain how features in the existing system works. Usually, the answers are of very high quality, and it is always easy to check the affected areas in the code. Even better is the fact that I can keep asking follow-up questions about parts that are still not clear to me. The purpose of this is always to increase my own knowledge of the system.
Conclusion 
These are extraordinary times, with LLMs changing a lot about how software is developed. I have found that using coding agents has changed how I spend my time as a developer. A lot of the incidental details of coding have gone away, while I am still engaged in the essential logic of what I am developing. Using Claude has also made understanding the existing code base a lot easier.
Share this: 
Share on X (Opens in new window) 
X 
Share on Facebook (Opens in new window) 
Facebook 
Share on LinkedIn (Opens in new window) 
LinkedIn 
Like Loading... 
Related 
This entry was posted in Programming , Testing , Work and tagged agent , AI , claude , LLM . Bookmark the permalink . 
← In Praise of –dry-run 
Leave a comment Cancel reply 
Δ 
MOST POPULAR 
Lessons Learned in Software Development 
Top 5 Surprises When Starting Out as a Software Developer 
Working as a Software Developer 
Great Programmers Write Debuggable Code 
What Makes a Good Programmer 
RECENT POSTS 
With Claude: Less Coding, More Testing 
In Praise of –dry-run 
Lessons From 9 More Years of Tricky Bugs 
More Good Programming Quotes, Part 6 
Programming Conference – Jfokus Stockholm 2025 
My Simple Knowledge Management and Time Tracking System 
Programming With ChatGPT 
John von Neumann – The Man from the Future 
Finding a New Software Developer Job 
Tidy First? 
What I Have Changed My Mind About in Software Development 
Well-maintained Software 
Algorithmic Trading: A Practitioner’s Guide 
There Is No Software Maintenance 
Switching to Go – First Impressions 
Effective Software Testing – A Developer’s Guide 
On Code Reviews 
Book Review: A Philosophy of Software Design 
On Comments in Code 
4 Things I Like About Microservices 
Recruiting Software Developers – Coding Tests 
More Good Programming Quotes, Part 5 
6 Small Unit Testing Tips 
Mathematical Modelling of Football 
Deployed To Production Is Not Enough 
Good Logging 
Working From Home – Cons and Pros 
Artificial Intelligence – A Guide for Thinking Humans 
20.5 Years of XP and Agile 
Secure by Design 
More Good Programming Quotes, Part 4 
Grokking Deep Learning 
EuroSTAR Testing Conference Prague 2019 
Classic Computer Science Problems in Python 
When TDD Is Not a Good Fit 
Recruiting Software Developers – Checking Out a Company 
Book Review: Designing Data-Intensive Applications 
Nordic Testing Days Tallinn 2019 
Book review: Accelerate 
More Good Programming Quotes, Part 3 
Programming: Math or Writing? 
Developer On Call 
My Favorite Command-Line Shortcuts 
6 Git Aha Moments 
Is Manual Testing Needed? 
Exercises in Programming Style 
Programming for Grade 8 
6 Years of Thoughts on Programming 
Benefits of Continuous Delivery 
More Good Programming Quotes, Part 2 
Developer Testing 
Programming Conference – QCon New York 2017 
Developers – Talk To People 
Code Rot 
Programmer Career Planning 
Software Development and the Gig Economy 
Book Review: The Effective Engineer 
Things Programmers Say 
Developer Book Club 
Book Review: Release It! 
18 Lessons From 13 Years of Tricky Bugs 
Learning From Your Bugs 
More Good Programming Quotes 
The Wisdom of Programming Quotes 
Ph.D. or Professional Programmer? 
Social Engineering from Kevin Mitnick 
Recruiting Software Developers – Initial Contact 
Coursera Course Review: Software Security 
Lessons Learned in Software Development 
Book Review: Clean Code 
Coursera Course Review: Computational Investing Part 1 
Programmer Knowledge 
5 Reasons Why Software Developer is a Great Career Choice 
A Response to “Why Most Unit Testing is Waste” 
What Makes a Good Programmer? 
Switching from Java to Python – First Impressions 
Antifragility and Software Development 
5 Unit Testing Mistakes 
Unit Testing Private Methods 
A Bug, a Trace, a Test, a Twist 
Session-based Logging 
Finding Bugs: Debugger versus Logging 
TDD, Unit Tests and the Passage of Time 
Automatically Include Revision in Log Statement 
7 Ways More Methods Can Improve Your Program 
LinkedIn – Good or Bad? 
Great Programmers Write Debuggable Code 
SET Card Game Variation – Complementary Pairs 
Programmer Productivity – Interruptions, Meetings and Working Remotely 
What Do Programmers Want? 
Coursera course review: Algorithms: Design and Analysis, Part 2 
Blog stats for 2012 (by WordPress) 
Working as a Software Developer 
4 Reasons Why Bugs Are Good For You 
Book Review: How Google Tests Software 
Top 5 Surprises When Starting Out as a Software Developer 
Programmer Productivity: Emacs versus IntelliJ IDEA 
Why I Love Coding 
Coursera course review: Design and Analysis of Algorithms I 
Mac OS X Break Programs Review 
Favorite Programming Quotes 
How I Beat Repetitive Stress Injury 
Introduction to Databases – On-line Learning Done Well 
10 million SET games simulated using “Random among ‘most similar’ Sets” 
10 million SET games simulated using “Random among available Sets” 
10 million SET games simulated using “First found Set” 
SET® Probabilities Revisited 
TAG CLOUD AI 
algorithms 
book 
book review 
break program 
bugs 
career 
code 
coding 
conference 
coursera 
creativity 
databases 
debugging 
developer testing 
DevOps 
emacs 
ergonomics 
face to face 
Google 
hiring 
history 
ide 
idea 
integration testing 
intellij 
interruption 
interviewing 
java 
job 
knowledge 
learning 
linkedin 
logging 
love 
machine learning 
Mac OS X 
math 
mathematics 
meeting 
meta 
methods 
office 
on-line course 
probabilities 
production software 
productivity 
professional software development 
programmer 
programming 
programming course 
programming job 
python 
quotes 
recruiting 
Repetitive Stress Injury 
review 
RSI 
security 
SET game 
simulation 
software development 
statistics 
stats 
stretches 
surprises 
tdd 
test-driven development 
testing 
trouble-shooting 
unit-test 
unit testing 
university 
work 
working RSS RSS - Posts RSS - Comments 
Follow Blog via Email 
Enter your email address to follow this blog and receive notifications of new posts by email.
Email Address: 
Follow 
Join 405 other subscribers 
Blog at WordPress.com. 
Comment 
Reblog 
Subscribe 
Subscribed 
Henrik Warne's blog 
Join 405 other subscribers 
Sign me up 
Already have a WordPress.com account? Log in now. 
Henrik Warne's blog 
Subscribe 
Subscribed 
Sign up 
Log in 
Copy shortlink 
Report this content 
View post in Reader 
Manage subscriptions 
Collapse this bar 
Loading Comments... 
Write a Comment... 
Email (Required) 
Name (Required) 
Website 
%d
