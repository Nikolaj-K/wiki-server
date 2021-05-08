First order logic up to strong set theory axioms. Axioms with constructive interpretation first.
Hello India.
====Preliminaries====
===Axiomatization strategy===
$\bullet$ Propositional logic (Give Lambda term justification)
$\bullet$ Predicate logic
$\bullet$ Predicate logic + Equality (as in Metamath - names also adopted directly)
$\bullet$ Weak form of CZF (Interpretable in MLTT. Point out topoi analogs.)
$\bullet$ Excluded middle (=ZF)
$\bullet$ Choice principle (=ZFC)
$\bullet$ Large cardinal
$\bullet$ Collapse

===Conventions===
We generally use letters for only one sort of thing throughout the text. Roughly:
$\bullet$ $x,y,z,u,A,a,f$ ... term or variables in predicate logic (here, generally sets variables, and $f$ will be a function/graph)
$\bullet$ $\varphi, \psi, \chi$ ... predicate (and earlier propositional) or "well-formed formulas" variables.
$\bullet$ $P$ ... a predicate name for some fixed, defined variable.
$\bullet$ $p$ ... a proof term or variable.
$\bullet$ Class notation $\{...\}$ is used (see Set notation and Impredicativity video)
$\bullet$ LaTeX's mathcal for set operations
$\bullet$ LaTeX's mathrm for very concrete predicates (see below)

$\bullet$ $\varphi\iff\psi$ ... $\varphi\implies\psi \land \psi\implies\varphi$
$\bullet$ $\exists !x. \varphi$ ... $\exists x. (\forall y. y=x) \land \varphi$ (bounded existential quantification)
$\bullet$ $\forall (x\in A). \varphi$ ... $\forall x. x\in A \implies \varphi$ (bounded universal quantification)
$\bullet$ $\exists (x\in A). \varphi$ ... $\exists x. x\in A \land \varphi$
$\bullet$ $\Finv x. \varphi$ ... $\forall x.(\varphi \implies (\forall x.\varphi))$, saying "$x$ is effectively not free in $\varphi$", i.e. "$\varphi$ is independent on the value of $x$". Usually not used unless you're super formal like we're here.
$\bullet$ $A\subset B$ ... $\forall x. x\in A\implies x\in B$

Without more details, we have standard notions:
$\bullet$ $\emptyset$ ... (implicitly defined in the conventional way using class notation)
$\bullet$ $\bigcup A$ ... the union of sets in $A$.
$\bullet$ ${\mathcal P}x$ ... power set of $x$
$\bullet$ $A\approx B$ ... The sets $A$ and $B$ are in bijection

Some symbols in other contexts are used for explanations, e.g. $f, g$ for lambda calculus terms (functions) in the standard way. And e.g.
$\bullet$ $(f\circ g)(x)$ ... $f(g(x))$ (only used in the discussion of proofs)

A sentence $\exists x. \varphi \land \psi$ will generally mean $\exists x. (\varphi \land \psi)$.
A sentence $\varphi \implies \psi \implies \chi$ will generally mean $\varphi \implies (\psi \implies \chi)$.
Unary operatisons (e.g. negations) bind stronger than binary ones.
Quantification binds generally very lax but (warning!) there could be cases where I oversaw something and this is not respected in this text.

No argument brackets as in $\varphi(x)$, but $\varphi$ represents the expression directly (that may syntactically have an x).
Only in explanations may we use the notation $P(x)$ and $P[y:=x]$ denotes $P$ with occurances of $y$ replaced by $x$.
E.g. if the particular predicate $P$ is $x=5$, then since we'll be able to prove $5=5$, the expression $P[x:=5]$ is provable.
Note that other variations of this abstracted subsititution notation are in use in some sources, e.g. brackets written on the left of the symbol instead of the right.

===Language===
class notation and more on pp.10-13 of
(Large Sets in Constructive Set Theory)
http://etheses.whiterose.ac.uk/8370/1/Ziegler%20--%20Thesis%20%28Hardbound%29.pdf

For some definitions, see p.7 of
(Constructive NF)
https://www.dpmms.cam.ac.uk/~tf/INF.pdf

e.g.
A set x is determinate iff (∀y)(y ∈ x ∨ ¬(y ∈ x));
A set x is stable iff (∀y)(¬¬(y ∈ x) → y ∈ x);
A set x is orthogonal iff (∀yz ∈ x)(¬¬(y = z) → y = z);
A set x is discrete iff (∀yz ∈ x)(y = z ∨ ¬(y = z));
A set x is inhabited iff (∃y)(y ∈ x);
A set x is nonempty if ¬(∀y)¬(y ∈ x).


===Metamath===
The bulk of axioms that follows are those from the IZF Metamath website (see reference section) although
the notation is occasionally adopted and the set theory is somewhat different, and so is the general order
of the axiom presentation within the different blocks.

Note for specialists:
The Metamath proof calculus works with subsitution and the theorems are really schemes of "setvar" variables.
In some logic presentations you have universal closures but this is not done there.
For this presentation, I have added universal closures in the form "For all $x$", etc., of all open variables in a separate line
to emphasize that the calculus should specify how to handle those.
The expressions with well-formed formula variables $\varphi, \psi$ is similarly preceeded with a "For all $\varphi, \psi$
", etc.
On the web page, you can find long discussion on their choices, and e.g. distinctness conditions on variables and such.
These questions are definitely important to write the fully formally verifier, but I can't properly add all their variable-related hints in the present overview.

====PROPOSITIONAL LOGIC Inference rules and Axioms====

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Rule of Modus Ponens

For all $\varphi, \psi$

$\dfrac{\varphi \hspace{1cm} \varphi \implies \psi}{\psi}$
</p>
Note that this is an inference rule. With conjunction $\land$ ("and"), the statement in the object language is a theorem and reads
$(\varphi \land (\varphi \implies \psi)) \implies \psi$

As an example (chosen interpretations of $\varphi$ and $\psi$) this e.g. says
"If it rains and if that it is raining implies that I'm wet, then I'm wet."
or, in a more constructive reading
"If {I have a reason to believe that} it rains and if {I have a reason to believe that} that {me having a reason to believe that} it is raining implies that {I have a reason to believe that} I'm wet, then {I have a reason to believe that} I'm wet."
or
"If {R} it rains and if {R} that {R} it is raining implies that {R} I'm wet, then {R} I'm wet."

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Axiom Simp

For all $\varphi, \psi$

$\varphi \implies (\psi \implies \varphi)$
</p>
"If {R} it rains, then if {R} I drank a coffee today, then {R} it rains."

$p \mapsto(q \mapsto p)$

$p_\varphi \mapsto(q_\psi \mapsto p_\varphi)$

$\lambda p. \lambda q. p$

$\lambda (p\colon\varphi). \lambda (q\colon\psi). p$

$\lambda (p\colon\varphi). \lambda (q\colon\psi). p\ \ \ \ \colon\ \ \ \varphi \implies (\psi \implies \varphi)$
<code>
def f(p):
    def g(q):
        return p
    return g
</code>

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Axiom Frege

For all $\varphi, \psi, \chi$

$(\varphi \implies (\psi \implies \chi)) \implies ((\varphi \implies \psi) \implies (\varphi \implies \chi))$
</p>
"If me being a Justin Bieber fanbody implies that if I'm on a Justin Bieber concert then I'll hyperventilate,
then if me being a Justin Bieber fanbody imlpies I'll be at the Justin Bieber concert, then
me being a Justin Bieber fanbody imlpies I'll hyperventilate."
(There's about 10 "have a reason to believe" clauses that could be inserted above)

$f \mapsto g\mapsto p\mapsto (f(p)\circ g)(p)$

$\lambda f. \lambda g. \lambda p. (f(p)\circ g)(p)$

Similarly, this directed contraposition law is "obviously true" using the function types-interpretation:
$(\varphi \implies \psi) \implies ((\psi \implies \chi) \implies (\varphi \implies \chi))$
Proof: $\lambda f. \lambda g. g\circ f$

For contrast, here's something that's not provable in this interpretation (and is indeed not a theorem of propositional logic):
$(\varphi \implies \psi) \implies \psi$
Not provable because generically, there's no way to obtain a function returing a value of type $\psi$.
(Also, compare this expression with modus ponens.)

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> AND-introduction

For all $\varphi, \psi$

$\varphi \implies (\psi \implies (\varphi \land \psi))$
</p>
"If I drank coffee today, then if my name is Nikolaj, then both, I drank coffee today and my name is Nikolaj.""

$\lambda p. \lambda q. \langle p, q\rangle$

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Left AND-elimination

For all $\varphi, \psi$

$(\varphi \land \psi) \implies \varphi$
</p>
If both, I drank coffee today and my name is Nikolaj, then, in particular, I drank coffee today."

$\lambda \langle p,q\rangle. p$

As noted, modus ponens in the object language reads
$(\varphi \land (\varphi \implies \psi)) \implies \psi$
and the proof is
$\lambda \langle p,f\rangle. f(p)$,
also called the application function.

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Right AND-elimination

For all $\varphi, \psi$

$(\varphi \land \psi) \implies \psi$
</p>
If both, I drank coffee today and my name is Nikolaj, then, in particular, my name is Nikolaj."

$\lambda \langle p,q\rangle. q$

The statement corresponding to Modus Ponens in the object language, $(\varphi \land (\varphi \implies \psi))\implies \psi$, is a theorem with proof $\lambda \langle p, f\rangle. f(p)$.

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Disjunction / Or

For all $\varphi, \psi, \chi$

$((\varphi \lor \psi) \implies \chi) \iff ((\varphi \implies \chi) \land (\psi \implies \chi))$
</p>
Note that this involves an "$\iff$", i.e. this can be understood as two related axioms.

$\Longleftarrow\ \ \ $ direction:
$\lambda \langle f, g\rangle. \lambda p. {\mathrm{if}}(p\colon\varphi)\ f(p)\ {\mathrm{else}}\ g(p)$

$\implies$ direction:
$\lambda f. \langle \lambda p. f(p), \lambda p. f(p)\rangle$

For a more non-constructive reading of OR and the case where $\varphi \lor \chi$ fails, recall that all implications will be true by explosion.

This second one is the only axiom in the list that's not always used to set up intuitionistic logic.
Similar to Axiom Simp, we might axiomize a disjunction-introduction as
$\varphi \implies (\varphi \lor \psi)$
which is a weakening (understood similar as a cast $n:{\mathbb N}$ into $n:{\mathbb Q}$),

Using the same interpretation of $\lor$ as in our proofs, it is easy to prove e.g.
$(\varphi \lor \psi) \implies ((\varphi \implies \chi) \implies ((\psi \implies \chi) \implies \chi))$

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> NOT-introduction

For all $\varphi$

$(\varphi \implies \neg \varphi) \implies \neg \varphi$
</p>
Note: $(\varphi \implies (\varphi\implies\psi)) \implies (\varphi\implies\psi)$ is valid via $\lambda f. \lambda p. f(p)(p)$
The axiom is then validated via the reading of $\neg \varphi$ as $\varphi\implies \bot$ with a propositional constant $\bot$ ("absurdity").

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> NOT-elimination / explosion

For all $\varphi, \psi$

$\neg \varphi \implies (\varphi \implies \psi)$
</p>
More difficult to justify computationally in a generic context, but e.g. realized in arithmetic via $\bot:=(0=1)$.
A use of NOT-elimination is the disjunctive syllogism $(\varphi \lor \psi)\implies (\neg\varphi \implies \psi)$.
The natural language are clear semantics are clear, although computationally it mirrors more of a consistency condition.

The law $\varphi \implies (\varphi \lor \psi)$ together with the disjunctive syllogism (considered as axiom) motivates explosion.
The disjunction-introduction usually pops up in natural deduction calculi but isn't part of the Metamath list of axioms either.

Final notes:
Consider the theorems
$\varphi\lor\psi \implies ((\varphi\implies\psi)\implies\psi)$,
and
$\varphi\land\psi \implies ((\varphi\implies (\psi\implies\chi))\implies\chi)$
Depending on the context/use and other axioms, these (with $\bot$ for $\chi$ in the second) may actually be used as definitions of AND and OR. See also: De Morgan's laws.
See also the higher order definition in the Calculus of Constructions. That calculus also includes a definition of negation in terms of implications and universal quantification.

====PREDICATE LOGIC Inference rules and Axioms====
In the following, $\varphi$ a priori depend on parameters $x, y,...$ from a "Domain of discourse".
The constructive calculus is similar to what we had with the proof terms.
But our domain of discourse is instead interpreted as whatever object are of interest to use.

Another informal comment:
Recall
$\lambda (p\colon\varphi). \lambda (q\colon\psi). p\ \ \ \ \colon\ \ \ \varphi \implies (\psi \implies \varphi)$
In our case, that will be sets. If we want to think of them as typed object, write $a:{\mathrm V}$ for some particular set $a$.
E.g. we may have some predicate $P$, possibly depending on a set parameter $x$ (consider $P$ being $\neg(x\in x)$),
and the propert $\forall x. P$ defined in terms of it ($\forall x.\neg(x\in x)$).
If some particular $x$-dependent proof expression $p$ is, for each $x$, an argument against for the corresponding $P$,
then we may think of a proof of the above property to be of the form
$\lambda (x\colon{\mathrm V}). p\ \ \ \ \colon\ \ \ \forall x. P$

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Rule of Generalization

For all $\varphi$

$\dfrac{\varphi}{\forall x. \varphi}$
</p>
Note that in the Metamath prover, you can prove theorem schemes, i.e. "For all" parameters, in the metalogic. So can translate a metalogical "For all" into the object language.

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Distinctness

For all $\varphi$

$\varphi \implies \forall x. \varphi$
</p>
Formalizing rule of independence.
Related to Generalization, except this isn't involving an isolated "$\vdash\ \varphi$".

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> $x$ is bound in $\forall x. \varphi$

For all $\varphi$

$(\forall x. \varphi) \implies \forall x. \forall x. \varphi$
</p>
Formalizing expression of a "syntatic intension".
Consider in light of Generalization.

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Axiom of Quantifier Commutation

For all $\varphi$


$(\forall x. \forall y. \varphi) \implies \forall y. \forall x. \varphi$
</p>
See currying + switch of pair elements.
Note that one could also just make sense of $\forall \langle x,y\rangle.$ and use projections, the allowed application of which isn't ordered.

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Axiom of Specialization

For all $\varphi$

$(\forall x. \varphi) \implies \varphi$
</p>
Compare with Generalization.
Mirrors Modus Ponens, but for all given $x$. (Compare $\forall x. \varphi$ with $\psi \implies \varphi$ for given $\psi$.)

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Almost converse Axiom of Quantified Implication

For all $\varphi$

$((\forall x. \varphi) \implies \forall x. \psi) \implies \forall x. ((\forall x. \varphi) \implies \psi)$
</p>
A more dependent variant of Specialization.
Pulling out $\forall$, ignoring an already bounded predicated.

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Axiom of Quantified Implication

For all $\varphi, \psi$

$(\forall x. (\varphi \implies \psi)) \implies ((\forall x. \varphi) \implies \forall x. \psi)$
</p>
Mirrors Axiom Frege.

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Define existential quantification

For all $\varphi, \psi$

$\forall x.(\varphi \implies (\forall x.\varphi)) \implies ( ( (\exists x. \varphi) \implies \psi) \iff \forall x. (\varphi \implies \psi) )$
</p>
The condition $\forall x.(\varphi \implies (\forall x.\varphi))$ (also abbreviated as $\bullet$ $\Finv x. \varphi$) says "$x$ is effectively not free in $\varphi$", i.e. "$\varphi$ is independent on the value of $x$". Usually not used unless you're super formal like we're here.

Just compare with the "Disjunction / Or" axiom, and consider $\exists$ a plural $\lor$ and $\forall$ a a plural $\land$.

Note:
Classically, $\exists$ and $\forall$ are related exactly like $\lor$ and $\land$ (See De Morgans law comment),
and then we only need to axiomize one quantifier and write $\exists x. \varphi$ for $\neg\forall x. \neg\varphi$.
Constructively, one may think of a proof of $\exists x. P$ as a pair:
$\langle a, p[x:=a]\rangle\ \ \ \ \colon\ \ \ \exists x. P$

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> $x$ is bound in $\exists x. \varphi$

For all $\varphi$

$(\exists x. \varphi) \implies \forall x. \exists x. \varphi$
</p>
Another formalizing expression of a "syntatic intension".
Consider in light of Generalization.

====PREDICATE LOGIC Axioms with equality====
There's an established general/generic axiomatic framework for equality but the axioms are nevertheless listed here in the concrete context for $\in$.

The constructive reading is that that the reflective property $a=a$ is validated by the value of a function $\mathrm{refl}$.
Although we won't dicuss Martin-Löf type subsitution rules here.
Here, again, we discuss the proof-calculus as in Metamath and so the axioms characterize equality and it's interaction with the other logic symbols.

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Axiom of Existence

For all $y$
$\exists x. x = y$
</p>
In principle proven by $\lambda y. \langle y, \mathrm{refl}(y) \rangle$, i.e. given any $y$, use that as $x$ and you got a winner.

(For the sake of it, we may well add an axioms saying there are at least two distinct things, i.e. $\exists x.\exists y. \neg(x=y)$ and then provide some constants.
Above I say in principle because, as noted, details here depend on how we formalize object language vs. meta-languasge etc.
But this term certainly expressed the property that we also have in mind.)

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Axiom of Equality

For all $x, y, z$
$x = y \implies (x = z \implies y = z)$
</p>
Transitivity. The common uncurried form reads $(x = y \land x = z) \implies y = z$.
The equality $y = z$ is constructively proven by substitution of the two sides with $x$, as granted by the antecedents.

Like this, the next two are also just subsitution laws of the form $x = y \implies (P(x) \implies P(y))$ with some particular unary predicates $P$.
(Note that here, for elaboration sake, we wrote $P(x)$ instead of just $P$.)

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Left Membership Equality

For all $x, y, z$
$x = y \implies (x \in z \implies y \in z)$
</p>
See above.

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Right Membership Equality

For all $x, y, z$
$x = y \implies (z \in x \implies z \in y)$
</p>
See above.

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Axiom of Quantifier Substitution

For all $x, y$
$(\forall x. x = y) \implies \forall y. y = x$
</p>
Formalizing in what way the variable name of the quantifier name does not matter. Implies
$\forall y. ((\forall x. x=y) \implies (\forall x. \varphi \implies \forall y. \varphi))$.

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Axiom of Bundling

For all $x, y$
$(\forall z. z = x) \lor (\forall z. z = y \lor \forall x. \forall z. (x = y \implies \forall z. x = y))$
</p>
It say a $z$ distinct from $x$ and $y$ doesn't affect the truth of $x=y$.
This is a somewhat technical axiom used in the subsitutition logic of the Metamath proof calculus.

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Axiom of Quantifier Introduction

For all $x, y$
$(\forall z. z = x) \lor ((\forall z. z = y) \lor \forall z. (x = y \implies \forall z. x = y))$
</p>
A variant of the Bundling axiom (just listed because Metamath does so too.)

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Axiom of Variable Substitution

For all $\varphi$

For all $x, y$
$x = y \implies ((\forall y. \varphi) \implies \forall x. (x = y \implies \varphi))$
</p>
Axiom for an introduction of an equality under a universal quantification.
Note that this involves a well-formed formula variable $\varphi$ as well.

====SET THEORY Axioms====
This has a predicate $\in$, interpreted as membership.
We can immediatenyl define notions such as the subset relation subsets $x\subset y$, e.g. as $\forall w. w\in x\implies w\in y$.

Let $x\simeq y$ denote $\forall z. (z\in x \iff z\in y)$, i.e. that the two sets $x,y$ contain the same thing.

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Axiom of Extensionality

For all $x, y$
$x\simeq y \implies x = y$
</p>
This says sets are equal (and thus can be substituted for one another)
exactly when they contain the same things, and nothing else matters.

Practically, the axiom gives us a means of proving equality of two sets, i.e. establish when they can be subsituted for another.

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Axiom of Pairing

For all $x, y$
$\exists u. \forall z. (z = x \lor z = y) \implies z\in u$
</p>
Think $u=\{x,y,\dots\}$ (See video on set builder notation and discussion of classes in Impredicativity video.)

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Axiom of Union

For all $x$
$\exists u. \forall y. (\exists z. y\in z\land z\in x) \implies y\in u$
</p>
Flattening, e.g. $u=\{x,y,z\}$ from $\{\{x,z\},\{y\}\}$.

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Axiom Schema of predicative Separation

For all $\varphi$

For all $x$
$\exists z. \forall y. y\in z \iff (y\in x \land \varphi)$

but, here, for predicativity sake, with all quantifiers in $\varphi$ bounded.
</p>
Read $\varphi$ as $\varphi(y)$.

Cut out subsets from any set via predicates.
This e.g. gives the empty set via set existence and any false predicate.

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Axiom Schema of of Replacement

For all $\varphi$

For all $d$
$(\forall (x\in d). \exists! y. \varphi) \implies \exists r. \forall y. (y\in r \iff \exists (x\in d). \varphi)$
</p>
Read $\varphi$ as $\varphi(x,y)$.

Generate (i.e. validate existence as sets) of classes characterized by a functional binary predicate.
At this stage we already have Cartesian products, equivalence classes or indexed sums (sum types).

There's also variants of this with more parameters universally quantified over.
Axioms up to here give you
the empty set $\emptyset$, pairs $\langle c, d\rangle$, e.g. modeled as the Kuratowski $\{\{c\},\{c, d\}\}$, and then Cartesian products $a\times b$ (sets of pairs).

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Axiom of Strong Infinity

$\exists w. \mathrm{Ind}\land \forall x. \mathrm{Ind}[w:=x]\implies w\subset x$

with $\mathrm{Ind}$ denoting $\emptyset\in w\ \land\  \forall (n\in w).\ (n\cup\{n\}) \in w$
</p>
Note: $\mathrm{Ind}$ was defined far above.
Also note that $P(a)\land \forall x. P(x)\implies a\subset x$ says that $a$ is minimal, among sets, w.r.t. a given property $P$.
Btw: This gives set existence.

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Axiom of Exponentiation

For all $x, y$
$\exists h. h = y^x$

with ... the superscript $y^x$ described below
</p>
Here $y^x$ (of $x\to y$) denotes the class of functional relations $f\subset x\times y$, i.e. those with $\forall (u\in x). \exists! (v\in y). \langle u, v\rangle \in f$.
For $y$ a set with more than one element, this gives characteristic functions. Classically $\{0,1\}^x\cong{{\mathcal P}}x$.
See also: Axiom of Powerset.

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Axiom Schema of Set Induction

For all $\varphi$

$(\forall y. \forall (x \in y). \varphi[y:=x] \implies \varphi) \implies \forall y. \varphi$
</p>
Read $\varphi$ as $\varphi(y)$.

"..."

I.e. the above can may be expressed as
For all $\varphi$

$(\forall y. \forall (x \in y). \varphi(x) \implies \varphi(y)) \implies \forall z. \varphi(z)$.
Note that propositions are vacuously true for elements of the empty set.
This Axiom roughly and effectively says that what is a set is something build up from the empty set, "the bottom".
See also: Regularity.

Compare with natural number induction, which we may write as
For all $\varphi$

$(\varphi[n:=0]\land\forall n. (\varphi \to \varphi[n:=n+1]))\ \to\ \forall n.\, n\varphi$
or, rewritten to mirror the Set Induction axiom,
For all $\varphi$

$(\forall n. (\varphi[n:=n-1] \to \varphi))\ \to\ \forall n.\, n\varphi$
Where $\varphi[n:=-1]$ is taken to denote a true statement (e.g. $0=0$, which is true by $\mathrm{refl}(0)$).

Natural numbers, their induction and arithmetic are of course model-able in this theory (PA, but formally Heyting airthmetic, since there's no LEM).
At this point we may add some stronger Collection axioms to do constructive analysis, while still being interpretable in Martin-Löf type theory (CZF).
We may further restrict the boundedness condition on the Separation Axiom Scheme and adopt the full powerset axiom (IZF).

====Non-constructive Axioms====
<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Law of Excluded middle

For all $\varphi$

$\varphi \lor \neg \varphi$
</p>
No real constrictive interpretation for this one,
but it's digestible if one passes from the "reason to believe" interpretation to on-the-nose truth.

With the constructive set theory axioms listed above, the theory now turns in ZF.
Note: If we want ZF, we wouldn't have to formulate power set in terms of function spaces.

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Axiom of Choice

For all $x$
$\neg(x=\emptyset) \implies \exists f. (f: x \to  \bigcup x) \land \forall (u \in x). f(u) \in u$
</p>
In ZF equivalent to well-ordering, which breaks the Existence Property.

We now have ZFC.

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Tarski Axiom

For all $x$
$\exists u. {\mathrm{GU}}$

with ${\mathrm{GU}}$ denoting $x\in u\ \ \land\ \ \forall (y\in u). ({\mathcal P}y \subset u\wedge {\mathcal P}y\in u)\ \ \land\ \forall (z\in{\mathcal P}u).(\neg(z \approx u) \to z\in u)$
</p>
See Grothendieck universe defined above. This axiom says that
For every set $x$, there exists a set $y$ whose members include the set $x$ itself, every subset of every member of $y$, the power set of every member of $y$ and every subset of $y$ of cardinality less than that of $y$.

This is Taerski-Grothendieck set theory and makes working with categories more convenient.

<p style="border:1px; border-style:solid; border-color:#ff66b3; padding: 1em;"> Falsehood

$\emptyset\in\emptyset$
</p>
A.k.a. $0=1$.
Everything is true (via explosion).

====References====
https://en.wikipedia.org/wiki/Frege%27s_propositional_calculus
https://en.wikipedia.org/wiki/Minimal_logic
https://en.wikipedia.org/wiki/Hilbert_system
https://en.wikipedia.org/wiki/Natural_deduction
https://en.wikipedia.org/wiki/Sequent_calculus
https://en.wikipedia.org/wiki/List_of_Hilbert_systems
https://en.wikipedia.org/wiki/First-order_logic#Equality_and_its_axioms

https://en.wikipedia.org/wiki/Brouwer%E2%80%93Heyting%E2%80%93Kolmogorov_interpretation
https://en.wikipedia.org/wiki/Curry%E2%80%93Howard_correspondence
https://en.wikipedia.org/wiki/Lambda_calculus

https://en.wikipedia.org/wiki/Calculus_of_constructions
https://en.wikipedia.org/wiki/System_F
https://en.wikipedia.org/wiki/Metamath

https://www.logicmatters.net/tyl/
https://www.amazon.com/Logic-Structure-Universitext-Dirk-Dalen/dp/1447145577
http://personal.psu.edu/t20/notes/
