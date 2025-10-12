# Introduction

## Table of Contents 

This presentation will go as follows:
- we first briefly introduce the semerédi regularity lemma, which from now on I will call simply regularity lemma (definitely not because I find it hard to pronounce)
- next we present stable graphs, a class of graphs that allow a stronger version of the regularity lemma
- it follows a sketch of the proof of this lemma, which reformulation is actually the main contribution of this thesis
- finally we will provide an application of this theorem in property testing, which aims at showcasing the strength or restricting to this class of graphs


---

# Semerédi's Regularity Lemma

## Idea semerédi Regularity Lemma

The semerédi Regularity Lemma is a well known result, and its idea is that all graphs can be partitioned in such a way that most pairs of parts behave in a quasi-random way.

In particular, it expects pairs to be regular, which is a property that (with some error) ensures that the edges of the pair are uniformly distributed between vertices.


## Regular partitions

Then, a partition is regular if most of the pairs are regular. 


## SzRL

Finally, the theorem states that for any regularity parameter epsilon, there is a not-too-large epsilon-regular partition where the parts are equally sized.

Crucially, the upper bound on the number of parts does not depend on the size of the graph, but only on the regularity parameter.
Otherwise, one could simply consider the singletons partitions, which is always regular.
This theorem has seen applications in many fields such as combinatorics, number theory, and computer science.


## Limitations of SzRL

However, this lemma suffers two major limitations:
- first the bound on the number of parts, although constant, is a power-tower function which height increases with the regularity, 
    and it has been proven unavoidable in the general case by Gowers.
- also, there are some irregular pairs, again something that is unavoidable and of which the half-graph is an example.


---

# Stable graphs and Stable Regularity Lemma

## Stable graphs

From this last point a natural question arises: do we still have this limitation if we avoid such graphs?
A half-graph is a bipartite graph that looks like this, and on the right we have its bi-adjacency matrix.
The graphs that avoid it are called stable graphs, and are the ones we will focus on for the rest of the presentation.
An important note is that this graph has bounded VC-dimension, a property that repeatedly appears during this work.


## k-order
Formally, we say that any graph with two sequences of k vertices satisfying the previous structure has the k-order property.
Then, a graph has the non-k-order property or is k-stable if it does not have the k-order property.
We note that the two sequences need not be disjoint, and any combination of edges may appear in each set of the bipartite graph.


## Other k-orders
Here we have an example of this last fact.
This graph has the 3-order property: a_1 and b_2 are identified in the same vertex, and we have extra edges a_2 a_3 and b_1 b_2.


## Stable Regularity Lemma
Finally, here we have the statement of the stable regularity lemma, where the number of parts is bounded by 
a polynomial in 1/epsilon, and there are no irregular pairs.

Additionally, all pairs have density either close to 0 or close to 1, but we need to note that this is not 
a core feature of stable graphs.
In fact, Fox-Pach-Suk proved that this happens in all graphs with bounded VC-dimension, which is a larger class 
of graphs containing that of stable graphs.


---

# Sketch of the proof

## Good sets

Proving this theorem requires introducing some new concepts.
First of all, we define epsilon-good subsets.

The idea is that, given a subset of vertices A...

...we want the following to be satisfied for each vertex b in the whole graph G:

- either b is mostly connected to A. 
In this case we say that the truth value of A with respect to b is 1.
Also, we denote overline-BAb, or the exceptional vertices of A with respect to b, the vertices of A that do not behave as the rest.

- or b is mostly not connected to A.
In which case the truth value is 0.

If this is satisfied by all vertices in the graph G, then A is epsilon-good.

Notice, that making the epsilon larger allows for more error, and thus the property is preserved by making the epsilon larger.


## Excellent sets

But the real property we care in this work is excellence, which in some way is a bidirectional version of goodness.

Consider an epsilon-good subset A.

Also consider a zeta-good subset B.

Since B is good, all vertices in A have either truth value 0...

...or truth value 1 with respect to B.

If one of the classes is very small...

... for all zeta-good sets B, then A is (epsilon, zeta)-excellent.

Notice that increasing epsilon again allows for a larger error w.r.t. each B, and decreasing zeta makes
the set of considered zeta-good sets smaller, both things making the property easier to satisfy.


## Non-monotone counterexample

It needs to be noted that the uni-parametric epsilon-excellence is not necessarily monotone in epsilon, and the graph in the screen 
is a counterexample.
This is something that is actually missed in the original paper, and accounting for this requires for some major changes
in the proof of the stable regularity lemma.


## Excellence implies regularity

But why do we care about excellence?

Well, it turns out that excellence implies regularity.
Thus, if we can partition the graph into excellent sets, we are done.
But do excellent subsets actually exist?


## k-tree

In order to prove this, we use a model theory structure called a k-tree.


## k-tree example

Here we represent a 3-tree, with branches b and nodes c.
The nodes are basically uniquely classifying the branches in a binary manner.
This notion is relevant in our context, as trees are strictly related with half-graphs.


## k-tree in half-graph

First of all, it is easy to see that we can find a k-tree in any sufficiently large half-graph.


## half-graph in k-tree

Most importantly, we can also find a bi-induced k-half-graph in any graph containing a sufficiently large k-tree,
but this is less trivial and requires using the unknown edges between branches and nodes. 


## Existence of excellent sets

We use this fact to prove the existence of excellent sets by contradiction.


## Existence of excellent sets - proof sketch

Assume that a sufficiently large subset A does not contain any not-too-small excellent subset.

Then, there exists an epsilon-good set witnessing that A is not excellent.

And thus we can find two somewhat large family of vertices in A, each from a different class of truth value with respect to B.

Since by hypothesis they are not excellent, we can repeat the process on each of these two sets.

And again...

... and again...

By carefully choosing vertices from each subset in this construction, we can build a k-tree, and, since this implies
k-order, we have a contradiction.


## Valued version

A similar result can be obtained ensuring that the sets have size from a predefined list of values.


## First partition

For any graph G, we can apply this result repeatedly to obtain a partition of G into excellent sets.
We take the graph, and extract an excellent set. 
We take the remainder of this operation and extract another excellent set.
And we keep doing this until the remainder is too small.
Now, this partition parts are not necessarily equally sized.


## Subsets of excellent sets

In order to address this issue, we ask ourselves: are subsets of excellent sets still excellent?

The answer is yes, with high probability but with slightly worse parameters.

The proof of this fact is actually very laborious, and has been the point that required
the most work to reformulate.
Specifically here is where the non-monotonicity of excellence in epsilon creates the most issues and needed to be corrected.
Still, given the time constraints, I will only mention the main tools used in this proof:
- we use the Sauer-Shelah lemma to bound the number of exceptional sets.
- an upper bound on the tail of the hypergeometric distribution to bound the probability of a random subset having
    a large intersection with an exceptional set.
- a double-counting argument on the exceptional vertices of random subset, together with the fact that the number 
    of exceptional edges between an excellent set and a good one is very small.


## Even partition of an excellent set into equally sized excellent parts

Since the probability of a random subset of an excellent set not being excellent is very small, we can use 
a union-bound argument to show that there must exist a partition of an excellent set into a given number of equally sized excellent parts.


## Refine partition into even one

We can apply this result to the uneven partition we obtained before, refining each part into equally sized excellent parts.


## Dealing with remainder

We still have some remainder in the partition, but this can be dealt with by distributing its vertices uniformly between 
all the parts, which only slightly worsens the excellence parameters of each part.


## Excellence theorem

Carefully choosing parameters we can put everything as a function of the desired regularity obtaining the following result.


## Stable Regularity Lemma

Finally, since excellence implies regularity, we have proven the stable regularity lemma.


---

# Property Testing

## Epsilon-test

We now give an application of this theorem to property testing to highlight the benefits of restricting to stable graphs.

So, given a property, we want an algorithm that is able to distinguish between graphs that satisfy the property and those
that are "far" from satisfying it, where far means that if we change the adjacency of a few pairs of vertices the graph 
still does not satisfy the property. 
The algorithm does not know the full input graph, but can ask for the adjacency of given pairs of vertices.
The number of queries required by the algorithm is called the algorithm complexity, and the goal is to reduce this number as much as possible.


## Testable properties

Ideal algorithms are these which complexity is constant with respect to the size of the input graph.
If there exists a constant complexity tester for a given property, we say that the property is testable.

A classic example of such a property is H-freeness, the property of not containing H as an induced subgraph.

It has been proven that, first this property, and later all hereditary properties are testable.
Still, the associated testers' complexity suffers from the huge bounds of the Regularity Lemma, so we study 
whether a nice complexity value can be achieved restricting to stable graphs.


## Unavoidability and abundance

A common strategy to approach this problem is proving that a graph G being far from H-freeness implies that there are many
copies of H as an induced subgraph of G.


## Reduced graph implies many copies of subgraph

First of all, consider a graph G and the reduced graph associated to a partition of G.
This reduced graph is basically a graph that has a vertex for each part of the partition, and two vertices are adjacent if
and only if the associated pair in the partition has high density.
We prove that: if this reduced graph contains a copy of H and the associated pairs in the partition are regular, then
there are many copies of H in G.


## Unavoidability implies abundance 

This is all that is needed to prove abundance if there is unavoidability.


## Graph H

Consider a graph H.
In this case we have a K_4 with two extra vertexes that are only adjacent to one vertex.


## Sketch in G

Also consider a k-stable graph G, which by the stable regularity lemma can be partitioned in such a way that all pairs are
either almost complete or almost empty.

That is, each pair can only have a very small number of exceptional edges, ...

... and we swap them to create a new graph G',...

...by unavoidability, the new graph G' still has some copy of H.

Now, each edge in this induced copy of H must come from a dense pair in G, and each non-edge comes from a not-dense pair 
in G.
Thus, we can apply the previous lemma proving that there are many copies of H in G, and we are done.


## The algorithm

The algorithm follows easily:
if the graph is far from being H-free, we have seen that it has many copies of the graph H, so querying the edges
between sufficiently many vertices, and checking whether there is or not a copy of H, is sufficient for answering
correctly with high probability.


## The bound

Here we have a bound on the abundance given by the theoretical result...

...and a bound on the query complexity of the provided algorithm.


---

# Conclusion

So to conclude:
- We provided a simplified and corrected version of the original proof of the Stable Regularity Lemma.
- We have given an application in property testing, achieving a uniquely clean proof of the testability of H-freeness
in stable graphs, leveraging the fact that the partition has no irregular pairs.
- Still, compared to other results in the context of graphs with bounded VC-dimension, the bound on the number of parts
of the Stable Regularity Lemma is exponential w.r.t. the stability while the other are only polynomial w.r.t. the VC-dimension
bound.
This suggests that the bound of the Stable Regularity Lemma may be improved to a polinomial exponent, and future work could go
on this line.
- Other lines, with the goal of leveraging the lack of irregular pairs, include testing for induced subgraphs that 
grow with the size of the graph, or moving from freeness testing to subgraph counting and estimation.


# Thank you

And this is it, thank you!




