=====Galilean group cohomology=====
====Lagrangians====
All

$L = \tfrac{m}{2}\left(\frac{{\mathrm d}}{{\mathrm d}t}q_t\right)^2 + \frac{d}{dt}\lambda(t, r(t))$

are equivalent w.r.t. a variation of the action that holds endpoints fixed.

Consider

$L=\tfrac{m}{2}\left(\frac{{\mathrm d}}{{\mathrm d}t}q_t\right)^2$

Independent of time and invariant of constand translations $q_t\mapsto q_t+d$ because
of the derivative. And $V^2:=V^T\cdot V$, so it's also rotationally invariant.
Boost/shearing:

$L_g := \tfrac{m}{2}\cdot \left(\frac{{\mathrm d}}{{\mathrm d}t}q_t + v\right)^2$

$= \tfrac{m}{2}\left(\left(\frac{{\mathrm d}}{{\mathrm d}t}q_t\right)^2 + 2 v^T q'(t) + v^2\right)$

$= L + m \left(v^T \frac{{\mathrm d}}{{\mathrm d}t}q_t + \tfrac{1}{2} v^2\right)$

$= L + m v^T \frac{{\mathrm d}}{{\mathrm d}t} \left(q_t + \tfrac{1}{2} v \cdot t \right)$

$= L + \frac{{\mathrm d}}{{\mathrm d}t} \xi_+$

$\xi_\pm = p^T \left(q \pm \tfrac{1}{2} v \cdot t \right)$ where $p\equiv mv$.

Abuse of notation: Explicit dependecies here: $\xi(q, t; g; m)$, with $q$ actually a functions of $t$, the
values of which are being acted upon by a transformation.
More abuse of notation: We'll use "$\xi$" also for a function of two group elements as well as one group element.

====QM====

$\hat{H}=i\frac{{\mathrm d}}{{\mathrm d}t}\ (\text{Schrödinger}), \hat{P} := -i\frac{{\mathrm d}}{{\mathrm d}q}$

$\hat{H}\Psi = E \Psi\ (\text{Eigenstate}), \hat{H} = \frac{1}{2m}\hat{P}^2 \implies E \Psi = \frac{p^2}{2m} \Psi$

Solution

$\hat{P}\Psi = p \Psi\ \Longleftrightarrow\ \Psi = c\cdot\exp(i\,(p^Tq-E\cdot t)) = c\cdot\exp(i\,\xi_-)$

Has
$\xi_-(t, q+tw, v+w) = \xi_-(t, q, v) + \xi_+(t, q, w)$

<code>
xi[pm_, q_, t_, v_] := m*v*(q + (pm*v*t)/2)
xi[-1, q+t w, t, v+w]-xi[-1, q, t, v]-xi[+1, q, t, w] // Simplify
also
xi[pm, pm2 ( q + pm v t), -t, pm2 v] - xi[pm, q, t, v] // Simplify
</code>
Both of those expression are zero.

====As cocycle====

At fixed $m$, as function $\xi \equiv \xi_+$ of two group elements $\langle t, q, v, R \rangle$:

$\xi(g', g) = m\, v'^T\, (R'\, q + \tfrac{1}{2} v' \cdot t)$

I.e. here velocity and rotation of $g'$ act on space and time of $g$
(the rotation $R$ was ignored for simplicity above),
although that in paritcular not at all a requirement for what follows.

Most importantly, $\xi$ fulfills the cocycle conditions:

$\xi(1, g)=0$ (evident)

$\xi(g', 1)=0$ (evident)

$\xi(g",g') + \xi(g"g',g) = \xi(g",g'g) + \xi(g',g)$ (not in the mood for that calculation)

This is an associativity relation on the group level for the extended group defined as follows:

$\langle {\mathrm e}^{i\theta'}, g' \rangle \cdot \langle {\mathrm e}^{i\theta}, g \rangle = \langle {\mathrm e}^{i\ \left(\theta'+\theta+\xi(g', g)\right)}, g'\cdot g \rangle$

====Equivalent cocycles====
At the same mass $m$, consider

$L_h := L+\frac{{\mathrm d}}{{\mathrm d}t}\left(-\frac{m}{2}\frac{1}{t}q_t^2\right) = \frac{m}{2}\left(\frac{{\mathrm d}}{{\mathrm d}t}q_t - \frac{1}{t}q_t\right)^2$

This is an equivalent Lagrangian that is explicitly invariant under $q_t\mapsto q_t+t\,v$. But it's not invariant anymore under space and time-translations.

On the group level, the cocycle turns out as

$\bar{\xi}(g', g) = mv^T\left(-q' + (v'+\tfrac{1}{2}v)\cdot t'\right)$

And $\bar{\xi}$ and $\xi$ are related by a coboundary term, i.e. they share an equivalence class.

====Some facts====
* The masses label the Lie-algebra representation (see commutation relation on Wikipedia) and
* so that's a 1-dim second cohomology.
* The group generated by different $m$ happen to be isomorphic (a phase speedup by $\frac{m_2}{m_1}$ doesn't change the circle group).
* Such cocycle's tie to projective representations.
* The Poincare group has trivial group cohomology (but you may still extend it that way).
* There's a Wigner and Erdal İnönü between the extensions of Poincare to Galilei (both then 11-dim) corresponding to the non-relativistic limit.

=====Literature=====
https://en.wikipedia.org/wiki/Group_extension#Central_extension
https://en.wikipedia.org/wiki/Group_cohomology#Projective_representations_and_group_extensions

https://www.cambridge.org/core/books/lie-groups-lie-algebras-cohomology-and-some-applications-in-physics/B570D04EC2EAA2A2C21BA23F245D2457
Lie groups, Lie algebras, cohomology, and some applications in physics-Cambridge University Press (1998)
Josi A. de Azcárraga, Josi M. Izquierdo -

Galilei Group and Galilean Invariance - JEAN-MARCLÉVY-LEBLOND
https://www.sciencedirect.com/science/article/pii/B9780124551527500112

Classical and Quantum Particles in Galilean and Poincaré Spacetime
Nesta van der Schaaf
https://www.math.ru.nl/~landsman/Nesta.pdf
Fiber perspective.

Galilei Group and Nonrelativistic Quantum Mechanics
https://aip.scitation.org/doi/10.1063/1.1724319
Jean‐Marc Levy‐Leblond

Foundations of Quantum Theory: From Classical Concepts to Operator Algebras,Klaas Landsman
https://link.springer.com/content/pdf/10.1007%2F978-3-319-51777-3.pdf
Discussion of group cohomology H^2 as relevant for QM. Discussion of Heisenberg group.
pp. 167+

Unitary representations of the Galilean line group: Quantum mechanical principle of equivalence
B. R. MacGregor, A. E. McCoy and S. Wickramasekara
https://arxiv.org/pdf/1107.2442.pdf

NEW INSIGHTS IN PARTICLE DYNAMICS FROM GROUP COHOMOLOGY
http://www1.jinr.ru/Archive/Pepan/v-33-7/16.pdf
Semi-classical theory with Poincare-Cartan forms made invariable

david-bar-moshe on SE, likes to answer question about symplectic geometry and
related mathematical physics concepts
https://physics.stackexchange.com/users/2190/david-bar-moshe

https://en.wikipedia.org/wiki/Heisenberg_group#On_symplectic_vector_spaces
https://en.wikipedia.org/wiki/Virasoro_algebra

https://en.wikipedia.org/wiki/Action_(physics)
https://en.wikipedia.org/wiki/Principle_of_least_action
https://en.wikipedia.org/wiki/Lagrangian_mechanics#Non-uniqueness
https://en.wikipedia.org/wiki/Free_particle
https://en.wikipedia.org/wiki/Lorentz_factor
https://en.wikipedia.org/wiki/Group_contraction

https://en.wikipedia.org/wiki/Klein%E2%80%93Gordon_equation#Relativistic_free_particle_solution
https://en.wikipedia.org/wiki/Relation_between_Schr%C3%B6dinger%27s_equation_and_the_path_integral_formulation_of_quantum_mechanics#From_Schr%C3%B6dinger's_equation_to_the_path_integral_formulation

https://en.wikipedia.org/wiki/Galilean_transformation