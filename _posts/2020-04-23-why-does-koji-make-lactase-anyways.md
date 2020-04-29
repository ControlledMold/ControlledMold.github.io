---
title: But why does koji make lactase?
image: assets/images/koji_lactase/header.png
tags:
- enzymes
- koji
- aspergillus-oryzae
- featured
categories:
- koji
---

An interesting question came up on the Koji subreddit about if one can make [lactose-free milk at home using koji](https://www.reddit.com/r/Koji/comments/g6lpnt/using_koji_to_make_lactose_free_milk/). The thread has some interesting replies, but I want to focus on an adjacent question that wasn't clear to me until I did some research. It's known that many fungi, including our friend Aspergillus Oryzae (koji), produce the enzyme lactase, which breaks down lactose into its subunits: glucose and galactose. See the Figure 1 below. (Lactase is also present in humans, but only into those who are not lactose-intolerant!)

[![lactase](/assets/images/koji_lactase/lactase.png)](/assets/images/koji_lactase/lactase.png){:target="_blank" .center}
*Figure 1. The lactase enzyme working on lactose sugar. Lactose is made up of glucose and galactose molecules.*


Research has shown that koji produces lactase on a wide variety of substrates, including wheat bran and spent beer grain - but these substrates don't contain lactose. In fact, the only natural source of lactose is mammalian milk, and koji didn't evolve to ferment milk. So why is koji producing lactase? What's going on?

### Why does koji produce lactase in the first place?

First, we note that lactase only acts on lactose (i.e. lactase has a very high _specificity_), so lactose must be present somewhere, else there would be no reason to produce lactase. Second, we note that lactase is an intracellular enzyme. From this, we can conclude that lactose is present _inside the cell_. Third: the koji is also "digesting" other carbohydrates, like starch, cellulose and hemicellulose. The former two are well known, but hemicellulose may not be. It's a carbohydrate that is found in plants (up to 30% of biomass), and contains a wide variety of sugars (not just glucose, the only sugar in cellulose). Galactose is one such sugar present in hemicellulose. When that galactose is attached to a glucose molecule, this looks like a lactose molecule. During digestion of hemicellulose by other enzymes (cellulase, etc.), the glucose-galactose a.k.a. lactose molecule is released.

[![hemicellulose](/assets/images/koji_lactase/hemicellulose.png)](/assets/images/koji_lactase/hemicellulose.png){:target="_blank" .center}
*Figure 2. Hemicellulose is a carbohydrate found in plants and made up of many different sugars. Enzymes acting on it will liberate smaller sugars, like lactose.*


This lactose molecule still needs to be broken down to be metabolized, hence lactase is needed (see Figure 1.). This solves the mystery of why fungi produce lactase.

### Can we affect the amount of lactase produced?

In [[1]](https://sci-hub.tw/10.1016/0168-1656(90)90065-J), the authors conclude that koji grown on a wheat bran substrate actually produces more lactase than a koji grown on whey (which is full of lactose). What explains that? The authors suggest that when lactose is high, a moderate amount of lactase will generate enough glucose and galactose that further lactase production is suppressed. Here's a high level explanation of why. With an abundance of lactose and some lactase present, intracellular glucose levels will be high, and there exists an internal feedback loop that halts further production of enzymes that aren't needed (like lactase) . So there exists an amount of lactase that balances this feedback loop. However, when lactose is limited, glucose is limited, and hence that feedback loop is never triggered, meaning that lactase is continuously produced.

[![lactose_substrate](/assets/images/koji_lactase/lactose_substrate.png)](/assets/images/koji_lactase/lactose_substrate.png){:target="_blank" .center}
*Figure 3. With abundant lactose in the cell, glucose levels spike and lactase production slows*

[![wheat_bran_substrate](/assets/images/koji_lactase/wheat_bran_substrate.png)](/assets/images/koji_lactase/wheat_bran_substrate.png){:target="_blank" .center}
*Figure 4. With limited lactose in the cell, glucose levels are lower (relatively) and lactase production continues*

#### References
 1. Bailey, M. J., & Linko, M. (1990). Production of β-galactosidase by Aspergillus oryzae in submerged bioreactor cultivation. Journal of Biotechnology, 16(1-2), 57–66. doi:10.1016/0168-1656(90)90065-j
