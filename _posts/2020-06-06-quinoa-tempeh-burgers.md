---
title: Time-lapse of quinoa tempeh burgers
image: assets/images/quinoa_burger/header.jpg
tags:
- plant-based
- umami
- recipe
- solid-state-fermentation
- tempeh
- sticky
categories:
- tempeh
---

I recently got my hands on some _Rhizopus Oryzae_ spores from [mycoboutique.com](http://www.mycoboutique.com/en/). Traditionally R. oryzae has been used to make tempeh. I've been making soy tempeh at home, which has been very tasty and better than store-bought tempeh, except for convenience (but whatever, I enjoy growing mold). The folks over at Noma had a different idea with what to do with R. oryzae: use it as a binder for a plant-based burger:

![Noma's burger](/assets/images/quinoa_burger/noma.png){:max-height="550" .center}
*From [Noma's Instagram](https://www.instagram.com/p/CApsk-lDiR7/)*


I wanted to try this ferment at home, and test out my new RaspberryPi camera. The camera is surprisingly good quality, and there's simple code from [`picamera` ](https://picamera.readthedocs.io/) to create a time lapse program. Below is my super janky photo studio in my incubator. The real work is being done by my helping-hands soldering tool:

[![photo studio](/assets/images/quinoa_burger/IMG_0799.jpg)](/assets/images/quinoa_burger/IMG_0799.jpg){:height="500" .center}
*My incubator's improvised photo studio. A helping-hand tool is holding up an LED light, a RaspberryPi, and a RapberryPi Camera.*

The ferment took about 22 hours in total at 30℃. By taking a photograph every 5 minutes, I could use imagemagick to create an animated gif of the growth over the duration of the fermentation.

![gif of growth](/assets/images/quinoa_burger/growth.gif)

If that went by too fast, here are the first and last photos, side-by-side:

[![before and after growth](/assets/images/quinoa_burger/sidebyside.jpg)](/assets/images/quinoa_burger/sidebyside.jpg){: .center}
*Initial patty vs 26h fermented patty.*

In the end, I had five nice "quinoa patties" bound together by the mycellium of _R. oryzae_. The smell was sweet and mushroom-y. The patties were very firm, easy to handle and transport as a single piece.

![end patty](/assets/images/quinoa_burger/sidebyside2.jpg){: .center}

I fried them in a pan with some olive oil, and seasoned them with yeast garum and soy sauce (as Noma recommended in their post). I served them on a bun with burger toppings. The taste: delicious! The mouthfeel: great! The quinoa patty did not crumble at all during cooking or eating. It had a firm texture - not mushy like most veggie burgers. In fact, I thought this was one of the best veggie burgers I've ever had.

![burger](/assets/images/quinoa_burger/IMG_0802.jpg){:max-height="500"  .center}


## Recipe

{::options parse_block_html="true" /}

<div class="recipe">

#### Quinoa tempeh patties

<div class="recipe-ingredients">

- 1.5 cups quinoa
- 1.5 cups water
- 1/8 cups vinegar (any type will do)
- 1 tsp tempeh starter

</div>

1. Rinse the quinoa well.
2. Added quinoa and water to pressure cooker. Once at high pressure, cook for 2.5 minutes. Let naturally cool to room temperature.
3. Add vinegar and mix well.
4. Add half the starter, mix; add other half, mix.
5. Portion into patty shaped containers. This amount was perfect for 5 old olive containers.
6. Ferment, uncovered, at 30℃ and moderate humidity (I keep a damp towel in the incubator). The temperature will spike after about 18h, so you'll want to try to keep an eye on it. It's likely the internal temp will reach close to 40℃ - that's okay.
7. The ferment will finish around 20h to 26h, depending on the temperature.
8. Cover and store in fridge to stop fermentation.

#### Burgers

<div class="recipe-ingredients">

- soy sauce mixed with yeast garum and 1:3 ratio.
- buns and burger toppings

</div>

1. Add an oil to a pan, and turn to medium-high pan. Once near smoking, add patties. Flip once underside is starting to brown, and apply yeast garum mixture to the top. Flip, and repeat. Let the patties darken more, but careful not to burn.
2. Make a burger. Enjoy!

</div>
