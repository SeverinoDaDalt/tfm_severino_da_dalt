# Introduction

## Table of Contents 

This presentation will go as follows:
- we first briefly introduce the semerédi regularity lemma, which from now on I will call simply regularity lemma (definitely not because it is hard to pronounce)
- next we present stable graphs, a class of graphs that allow a stronger version of the regularity lemma
- it follows a sketch of the proof of this lemma, which reformulation is actually the main contribution of this thesis
- finally we will provide an application of this theorem in property testing, which aims at showcasing the strength or restricting to this class of graphs


---

# Semerédi's Regularity Lemma

## Idea semerédi Regularity Lemma

The semerédi Regularity Lemma is a well known result, and its idea is that all graphs can be partitioned in such a way that most pairs of parts behave in a quasi-random way.

In particular it expects pairs to be regular, which is a property that (with some error) ensures that the edges of the pair are uniformly distributed between vertices.


## Regular partitions

Then, a partition is regular if most of the pairs are regular. 


## SzRL

Finally, the theorem states that for any regularity parameter epsilon, there is a not-too-large epsilon-regular partition where the parts are equally sized.

Crucially, the upper bound on the number of parts does not depend on the size of the graph, but only on the regularity parameter.
Otherwise, one could simply consider the singletons partitions, which is always regular.
This theorem has seen applications in many fields such as combinatorics, number theory, and computer science.


## Limitations of SzRL

However, this lemma suffers two major limitations:
- first the bound on the number of parts, although constant, is a power-tower function, which has been proven unavoidable in the general case by Gowers.
- also, there are some irregular pairs, again something that is unavoidable and of which the half-graph is an example.


---

# Stable graphs and Stable Regularity Lemma

## Stable graphs

From this last point a natural question arises: do we still have this limitation if we avoid such graphs?
A half-graph bipartite graph that looks like this, with its respective bi-adjacency matrix.
The graphs that avoid this graph are called stable graphs, and are the ones we will focus on for the rest of the presentation.
An important note is that this graph has bounded VC-dimension, a property that repeatedly appears during this work.


## 