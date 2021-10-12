# Backyard Hacks 2.0 - Major League Hacking
- Best use of Google Cloud

## Inspiration 💡
The advent of the 𝐂𝐨𝐯𝐢𝐝-𝟏𝟗 has turned all of our lives upsides down. Changes in social dynamics due to local restrictions impacted human behavior and led to a shift in **business** dynamics. With that, a boom in the online marketplace is also prominent. Social media presence is helping people such as small businesses and organizations make a smart move, especially after seeing the effect that the COVID-19 Pandemic has left on the same. Many small businesses are struggling to stay open during these difficult times due to the lower count of people. This is indeed a very serious problem that is becoming the root cause of economic downfall in most countries.

![logo](https://ipfs.infura.io/ipfs/QmWoEdX6YyDoNzLXYsNu79odw8QnUnu6qMXqrkUhUT6gmr)

We believe that with the power of AI, this can be solved if proceeded creatively. Thus we made **Social Curator**! 


## What it does 🤔
**Social Curator** is a smart web-app that is built for helping small business owners gain the social media traction they need to keep their doors open. We hope to make the lives of marketers, business people, and influencers on social media easier, so they don't have to search for **#hashtags** and decide which ones are the best themselves, instead they can rely on our app to decide the same automatically.

Hashtags are a surefire way of boosting impressions, improving content searchability, and encouraging more people to talk about the brand. Moreover, it can easily help people finding social media content, increase social media engagement, and attract new customers etc. Choosing the right hashtags for a post can help it sky-rocket in popularity – gaining your content views, likes, re-tweets, and shares. All of this social activity ultimately helps to amplify content and business exposure. But, not all hashtags are created equal. And different types of hashtags reach different audiences – accomplishing different goals for the business. And the best part is that, nobody owns a hashtag. You can’t trademark hashtags, anybody can use them, and they can be any combination of words or phrases. We carried out a research & found that there are around 7+ popular platforms that support #hashtag boosts. For this project, we have moved forward with Instagram since few surveys describe Instagram as the most popular social networking app.

![x1](https://ipfs.infura.io/ipfs/QmSEE2iHESQD5E6Tu9j4WHGyNTgrY5Ka3gWaWbFETSNrEi)

![x2](https://ipfs.infura.io/ipfs/QmZC1rZci4uZguxiPe4cjoyFWrKNm7ApgB9W5KKagYrnvA)

![x3](https://ipfs.infura.io/ipfs/QmULTpJsyJywQMMgmfMQGAWSfQrLYVbuARWSYDzPeG5nfd)

Once logged in, it provides the most relevant and popular hashtags for social media posts, bringing in larger audiences that are more likely to interact with the user’s content. All the user has to do is upload the picture that they want to post on our website. Then, the image is passed through an ML model which does the feature extraction & classifies the same. After processing, we return a suitable caption & a list of relevant trending hashtags (sorted in relevant-frequency order).

Wait, that's not the end. We also provide some analytics & SEO of the same image depending upon few classification factors like — (i) Quality, (ii) Resolution & (iii) Compression & generate a Word-Cloud from the frequency count of those keywords. Once we're done, we redirect the user to the posting page.


## How we built it ⚙️
**Social Curator** is crafted with ❤️. The front-end is made in React.js with Tailwind CSS. The authentication is done via Firebase. The backend is running on GCP's instance and for the feature extraction & classification, we're using Inception-v3 trained with ImageNet [refined hyperparameters & underfitted (x0.65)] as the dataset. The tech stack of the project is mentioned below :—

![logo](https://ipfs.infura.io/ipfs/QmecLLsGbUhvUWnP5SA1m58kVcK8wrZZfsrJsSxm9k1yHz)

The ML pipeline is as follows :—
![pipeline](https://ipfs.infura.io/ipfs/QmVyNT3PfmrBUKbMd1Bq7K6keVqqSxriQ5zupRA24JEnbe)


## Challenges we ran into 😤
**A lot!** As I previously mentioned, the whole execution was done from scratch, even the advent of idea in our mind literally came during the opening ceremony from Joyce. We broke the timeline into small chunks & divided the tasks among us depending on priority. Joyce was the product manager for us. Arnab was primarily working on the Front-end while Pratyay was working on the integrations & backend. Besides, he also worked on building the ML model & cooked the API. We faced most challenges while using those APIs when we were integrating the modules into one. But later on Pratyay managed to make a bypass method that returns the #Hashtag frequencies using **Rapid-API**. Last but not the least, it was a bit difficult for us to collaborate in a virtual setting but we somehow managed to finish the project on time.

---
## Design

We were heavily inspired by the revised version of **Double Diamond** design process developed by **UK Research Council**, which not only includes visual design, but a full-fledged research cycle in which you must discover and define your problem before tackling your solution.

![Double-Diamond](https://ipfs.infura.io/ipfs/Qmdy6iR3qoSRzrQrtRScVAdSmw9ECbmAXqE3mxMsU3AKNe)

> 1. **Discover**: a deep dive into the problem we are trying to solve.
> 2. **Define**: synthesizing the information from the discovery phase into a problem definition.
> 3. **Develop**: think up solutions to the problem.
> 4. **Deliver**: pick the best solution and build that.

This time went for the minimalist **Material UI** design. We utilized design tools like Figma,  Photoshop & Illustrator to prototype our designs before doing any coding. Through this, we are able to get iterative feedback so that we spend less time re-writing code.

![Brand-identity](https://ipfs.infura.io/ipfs/QmT3vyZYY2Aw6pX4o6hfCzzmW9Aw9RJ4udjfQmRZGCC2ee)

---
# Research 📚

- Neural Image Caption Generator, *Google Research* : https://arxiv.org/pdf/1411.4555.pdf
- Image Classification with Classic and DL Techniques, *ArXiv [May 2021]* : https://arxiv.org/pdf/2105.04895.pdf
- Multimodal DL approach for NER from social media, *ArXiv [Jul 2020]* : https://arxiv.org/pdf/2001.06888.pdf
- Attention based Selection Mechanism for Hashtag Generation, *ArXiv [Jun 2021]* : https://arxiv.org/pdf/2106.03151.pdf
- “TL;DR:” Out-of-Context Adversarial Text Summarization and Hashtag Recommendation, *ArXiv [Apr 2021]* : https://arxiv.org/pdf/2104.00782.pdf


♣ Dataset :- [ImageNet](https://www.image-net.org) 

♣ Model :- [Inception-v3](https://keras.io/api/applications/inceptionv3)

♣ Articles :-
- Hashtags for different Social Media platforms, *DigitalReady* : https://bit.ly/3ubw9bw
- Valuable Hashtag Marketing Strategies Proven to Engage Audiences, *Keyhole* : https://bit.ly/2XLNKuA
- Why Hashtags Matter to Your Brand, *Loomly* : https://bit.ly/39CHE2a
- Why Hashtags are important in digital marketing, *ThriveHive* : https://bit.ly/39G2z4K 
- 5 Reasons Why Instagram Hashtags Are Important, *NewBirdDesign* : https://bit.ly/3oa0sP4
- How to grow business using Hashtags, *Forbes* : https://bit.ly/2ZvBLlP
- COVID-19: Implications for business, *McKinsey* : https://mck.co/3kFwTm8
- How COVID-19 triggered the digital and e-commerce turning point, *UNICEF* : https://bit.ly/3uelRYd
- COVID-19 Effect on Online Shopping : https://bit.ly/39CIvjo

**CREDITS**
- Design Resources : Freepik
- Icons : Icons8
- Font : Recoleta / Manrope / Montserrat / Roboto

---
# Takeways
### Accomplishments that we're proud of ✨
We are proud of finishing the project on time which seemed like a tough task as we started working on it quite late due to other commitments and were also able to add most of the features that we envisioned for the app during ideation. Moreover, we learned a lot about new web technologies and libraries that we could incorporate into our project to meet our unique needs. And as always, working overnight was pretty fun! :)

### What we learned 🙌
**Sleep is very important!** Jokes apart, tbh a lot of things, both summed up in technical & non-technical sides. For the technical part, we did face some serious issues while we're finetuning the hyperparameters. Handling CORS and other bugs were also a big challenge. We also gave our level best to make the UI/UX look solid which helped us learn more about different design-centric approaches! Not to mention, Stackoverflow was the gem for us while we're troubleshooting some complicated issues late-night.

### What's next for Social Curator 🚀
We just really want this project to create a real positive impact on humanity. We are planning to integrate some cosmetic features into the application to make the UI look more attractive & intuitive. We are also looking forward to improving machine learning model performances, and adding cross-platform support. Moreover, a lot of code needs to be refactored as we couldn't hit so much under 36 hrs. Overall, we hope that one day this project can be widely used globally to help small businesses & startups amplify with ease.

**Note** — **API credentials have been revoked. If you want to run the same on your local, use your own credentials. Seok Left the team**

![footer](https://ipfs.infura.io/ipfs/QmRFfhA2i7yXTGfmBaQNpPh1GcezMFLhbTTMk2q813nLzj)
