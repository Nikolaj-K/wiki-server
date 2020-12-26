====The Continuum Hypothesis and its consequences====
===have been a disaster for integration theory===

Let $I:=[0,1]$ be the real unit interval.
Consider the ordinal $\beta$ with $|\beta|=|I|$ and $b\colon I\to\beta$ the corresponding bijection.

Let
$s:I\times I\to \{0,1\}$
$s(u,v) := 1 {\text{ if }} b(u) < b(v) {\text{ else }} 0$

Denote by $Sub$ be the claim that if a set $y$ is bigger than another set $x$,
then it also has more subsets.

If $Sub$ holds, then the theorem allowing to switch the integrals in
$\int_0^1\int_0^1 s(x,y)\, {\mathrm d}x\,{\mathrm d}y$
 (a.k.a. Fubini-Tonelli) doesn't hold for $s$.

----

$x=\{a,b\}$
$|x|=2$

${\mathcal P}x=\{\{\},\{a\},\{b\},\{a,b\}\}$
$|{\mathcal P}x|=4=2^2$

$y=\{a,b,c\}$
$|y|=3$

${\mathcal P}y=\{\{\},\{a\},\{b\},\{c\},\{a,b\},\{b,c\},\{c,a\},\{a,b,c\}\}$
$|{\mathcal P}y|=8=2^3$

$2<3\ \ \land\ \ 2^2 < 2^3$

$5<9\ \ \land\ \ 2^5 < 2^9$

$\forall ( m,n \in {\mathbb N} ). m < n \implies 2^n < 2^m$

----

$\forall x, y. |x|<|y|\implies |{\mathcal P}x|<|{\mathcal P}y|$
?

$\forall x, y. |x|<|y|\implies |x\to\{0,1\}|<|y\to\{0,1\}|$
?

$|{\mathbb N}|<|S|\ \ \land\ \ |{\mathcal P}S| = |{\mathcal P}{\mathbb N}|$
?

$|{\mathbb N}|<|S|\ \ \land\ \ |S| < |{\mathcal P}{\mathbb N}|$
?

$|{\mathbb N}|<|S|\ \ \land\ \ |{\mathcal P}S| = |{\mathbb R}|$
?

$|{\mathbb N}|<|S|\ \ \land\ \ |S| < |{\mathbb R}|$
?

Note:
Constructively, $x\to\{0,1\}$ has an easier time of being a set than ${\mathcal P}x$.
But in a classical theory there's no difference.

$S \subset {\mathbb R}$
$|{\mathbb N}| < |S|$

$|S| = |{\mathbb R}|$
?
(CH)

Note:
For expressing CH in this and that formulation, you may or may not
need well-ordering theorem / Axiom of Choice.
(And I'll assume them in this video where necessary.)

----

Refresher: von Neumann ordinal sets.

Empty set
$\{\}=\{x\mid \neg (x=x)\}$

Successor set
$Sx\equiv x\cup\{x\}$

$0\equiv \{\}$
$1\equiv S0=\{0\}$
$2\equiv S1=\{0, \{0\}\}=\{0, 1\}$
$3\equiv S2=\{0, \{0\}, \{0, \{0\}\}\}=\{0, 1, 2\}$
$n+1\equiv Sn$
$\dots$

$\alpha<\beta\equiv \alpha\in\beta$

$\omega_0 = \{0,1,2,3,4,5,\dots\}$ (limit ordinal)
$\omega_0+1 = S\omega_0$
$\omega_0+2 = S(\omega_0+1)$
...
$\omega_0\cdot 2 = S\omega_0$ (limit ordinal)
$\omega_0\cdot 2+1 = S(\omega_0\cdot 2)$
...
$\omega_0^7 + 5$
...
$\omega_0^{\omega_0} + 69$
...
$\omega_1 \equiv  \omega_0 \cup I$ (limit ordinal)
where $I$ is the set of all all countably infinite ordinals, $\{ \alpha\mid\mathrm{Ord}(\alpha) \land |\alpha|=|\omega_0| \}$.
$\omega_1 + 1 \equiv S\omega_1$

($\aleph_0\equiv|\omega_0|, \aleph_1\equiv|\omega_1|$)

----

$|\omega_1| = |\omega_0\to\{0,1\}|$

$|\omega_1| = |{\mathbb R}|$
? (CH)

Note:
More cauciously, use class of hereditarily transitive countable sets in place of $\omega_1$
(that formulation assumes less ordering).

CH category theoretically:
In a sequence of mono's $N\hookrightarrow S\hookrightarrow \Omega^N$,
with $N$ a natural number object, $\Omega^N$ the exponentiated truth values,
either is an iso.
(E.g. consider ${\bf{Set}}$ with $N={\mathbb N}$ and $\Omega=\{0,1\}$.)

----

Let $I:=[0,1]$ be the real unit interval.
Consider the ordinal $\beta$ with $|\beta|=|I|$
and $b\colon I\to\beta$ the corresponding bijection.

Define

$s:I\times I\to \{0,1\}$

$s(x,y) := 1 {\text{ if }} b(x) < b(y) {\text{ else }} 0$

===Theorem:===
CH $\implies$ $s$ is not measurable.

===Proof:===
CH says $\beta=\omega_1$. Then
$\bullet$ For each $y$, the set $\{x\in I\mid s(x,y)=1\}$ is a null set since
there's only countable many $x$ smaller than $y$.
$\bullet$ For each $x$, the set $\{y\in I\mid s(x,y)=1\}$ is the compliment of
a null set in the same way as above.
So if $s$ is measurable, the Fubini-Tonelli theorem gives

$0=\int_0^1\int_0^1 s(x,y)\, {\mathrm d}x\,{\mathrm d}y = \int_0^1\int_0^1 s(x,y)\, {\mathrm d}y\,{\mathrm d}x = 1$

----

Cohen/forcing:
Roughly...
$\omega_2\times\omega_0\to\{0,1\}$
or
$\omega_2\hookrightarrow(\omega_0\to \{0,1\})$ in a ZFC model.
$\implies$
$|\omega_1| < |\omega_0\to \{0,1\}|$ can't be disproven from a consistent ZFC.

Moral:
The set of subsets of the natural numbers is "very flexible"/"can be a lot of sizes".

===References===
https://en.wikipedia.org/wiki/Continuum_hypothesis
https://www.math.tamu.edu/~roquesol/History_of_Continuum.pdf
https://plato.stanford.edu/entries/continuum-hypothesis/
http://logic.harvard.edu/EFI_Feferman_IsCHdefinite.pdf
https://en.wikipedia.org/wiki/First_uncountable_ordinal
https://en.wikipedia.org/wiki/Fubini%27s_theorem
https://en.wikipedia.org/wiki/Solovay_model
