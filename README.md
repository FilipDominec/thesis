===== BIG LIST OF all TODOs as of 2015-11-23 =====
 * [X] acknowledgements
 * [X] ... abstract + its translation
 * [ ] mm-phc boundary add refs, add some quotations from papers, (and review again)
 * [X] metamaterial homogenization
 * [X] "negative-index", "left-handed" or "doubly-negative" media?
 * [X] FDFD
 * [-] SKIPPED - PWEM principle
 * [X] initial effparam branch, weaknesses of the method
 * [X] CDH: full
 * [X] other effparam retrieval methods (TODO review)
 * [ ] sieving: add statistics of spheres
 * [X] 'Mechanical drilling of fishnets'
 * [X] 1	Dielectric slab
 * [X] 2	Wire medium
 * [X] 3	Cut wires: rev
 * [X]		prepare THz-TDTS data for Bousek samples?
 * [ ]		compare them with a FDTD simulation
 * [X] 4	Electric-magnetic resonators
 * [X] 5	Split-ring resonator: comment double-strip
 * [X] 6	Dielectric sphere: introduce Mie resonances
 * [ ]		prepare THz-TDTS data for diffeernt size fractions
 * [X] 7	SRRs and spheres in a wire array or grid
 * [/] 8	Dielectric rods parallel to magnetic field
 * [/] 9	Dielectric rods parallel to the electric field
 * [X]		compare the OpEx2014 results with CDH? 
 * [ ] 10	Metallic sheet with slits
 * [ ] 11	Fishnet - metallic sheet with holes
 * [X]		prepare THz-TDTS data from the laser-machined sample
 * [-]		prepare THz-TDTS data from the drilled sample?
 * [ ] 12	Other structures
 * [/] Conclusion
 * [-] SKIP comment on the tunability of various structures - parametric scans of results etc.
 * [-] SKIP Write a correct definition of effective eps and mu??

==== Experimental data ====
 * [X] Experimental data: fishnet 28a, 28c
 * [/] Spheres: compare N for three sieved samples, (do they have granulometry?)
		(source /home/filip/PhD/Granulometry/120531_mikrofoto_trepacka/2012.05.31.ts1)
 * [ ] Cut-wires: Bousek "blue" sample (from 2014.09.10_MMonSi.ts1)
 * [ ] Spheres - permeability spectra convolution - replot 
		somewhere is the granulometry, see PNG figure /home/filip/PhD/Output_web/img
 * [ ] Au-Mylar-Au fishnet? Decide if reasonable.
 * [-] SKIP drilled fishnet (
		(note it is first measured in 2012-03-14_TiO2_powder.ts1 between sapphire slabs, but not used?)
 * [ ] find some sieving histograms and statistics?


==== Finally ====
 * [ ] attach the list of own publications
 * [ ] Use correct citation style!
 * [ ] results: make sure that |r| are |t| denoted correctly as modulus, not the actual complex value
 * [ ] make list of figures, adding short caption to each of them? -- and link to the simulation directory
 * [ ] resolve that `t' denotes transmittance and time simultaneously?
 * [ ] ...ize ---> ...ise 
 * [ ] go through all TODOs
 * [ ] make index of kwords https://en.wikibooks.org/wiki/LaTeX/Indexing?
 * [ ] aa 'of this' -->   'its' or  'thereof'  (and similar)
 * [ ] aa [a-z]-[a-z] *tex
 * [ ] aa transmi[^t]
 * [ ] check for dupli words /\(\<\S\+\>\)\(\_\s\+\<\1\>\)\+
 * [ ] some figures should change from a)  to  (a) etc.
 * [ ] generate nice polar plots (Smith charts) for normal and Fano resonances?
 * [ ] review the abstract

==== Ideas =====
%Two oscillators with nearly the same frequency:
%electric+electric or magnetic+magnetic → strong coupling, leads to twice curled curve in polar plot
%electric+magnetic → weak or no coupling (magnetic dipole: H field even, Efield odd; electric dipole: H field odd, E field even → may be regarded as zero inner product of the field functions)
%interpreting resonance (and Fano-resonance) curves
	%wave in free space → s12 ampli constant, phase constantly growing; (s11 zero)
	%→  in polar plot: a clockwise rotating unit vector
	%reflective surface → s11 ampli constant, phase constantly growing; (s12 zero)
	%simple resonance (in SRR?) 
	%→  reflectance peak
	%if fres1 < fres2 → …





A serious applicant will lists the following items separately, when applying for a job or applying for promotion:

*    List of refereed papers. With *all* the authors and also in the order in which they appear in the journal. In case of an extreme long list (more than ten), say at least how many co-authors there are . In addition report the number of published pages each article entails.
*    List of conference proceedings, if  they cannot be classified as peer-reviewed. Again with all the authors. And again state the number of published pages for each item.
*    List of popular papers. With all the authors and with the number of published pages.
*    List of invited talks at international conferences, with the names of co-authors if applicable.
*    List of invited individual talks delivered at scientific institutes.
*    List of contributed talks to international conferences, with the names of all other co-authors and in the correct order.
*    List of posters, with the names of all other co-authors in the correct order.




















%\paragraph{Principles of PWEM for one-dimensional nonmagnetic PhC} 
%Unlike FDFD, PWEM is based on direct and more efficient solution of a linear algebraic problem:
%\begin{equation} 
	%{\epsrl}^{-1}(\omega,\rr) \nabla\times \left[{\murl}^{-1 }(\omega,\rr) \nabla\times \E(\rr) \right] = \frac{\omega^2}{c^2}\E(\rr),  \tag{\ref{eq_eigen_e} \again}
%\end{equation}
%where ${\epsrl}^{-1}(\omega,\rr)$ and ${\murl}^{-1 }(\omega,\rr)$ are user-defined with a known periodicity, but $\omega$ nor $\E(\rr)$ are not known.
%
%In one dimension and without magnetic effects, Eq. (\ref{eq_eigen_e}) simplifies to 
%\begin{equation} 
%{\epsrl}^{-1}(\omega,x) \frac{-\mathrm{d}^{2}}{\mathrm{d}x^{2}} \E(x) = \frac{\omega^2}{c^2}\E(x),  \label{eq_eigen_e1d}
%\end{equation}
%
%Thanks to periodicity, the structure permittivity can be expanded to a Fourier series with complex coefficients: 
%\begin{equation} \epsrl(x) = \sum_{q=-\infty}^{+\infty} \epsrl_q e^{-i 2\pi q x/a},  \label{eq_}\end{equation}
%where the zeroth coefficient $\epsrl_0$ denotes the zero spatial frequency, i.e. it is given by the average permittivity in the unit cell.  Likewise, the field $\E(x)$ can also be expanded as
%\begin{equation} \E(x) =  \sum_{q=-\infty}^{+\infty} \epsrl_q e^{-i 2\pi q x/a - i k x},  \label{eq_}\end{equation}
%where the zeroth coefficient $E_0$ has again the lowest spatial frequency, but it accounts for possibly nonzero wavenumber $k$ in the exponent.
%
%Importantly, the components
%
%\paragraph{Principles of PWEM for one-dimensional nonmagnetic PhC} 

%% \subsection{Transfer-matrix method} % TODO??

%% \paragraph{Principles of TMM} 
%% \add{
%% The \textit{transfer-matrix method} (TMM, or also \textit{Abelès formalism} %% ref Abeles1950: recherche sur la propagation des ondes electromagnetiques...
%% ) provides an analytically exact and notably simple computation of the transmission of one-dimensional, layered structures. It has been applied e.g. for the design of antireflective layers, dielectric mirrors, defect-mode filters etc. It shall be noted that extensions of TMM for two- or three-dimensional computation also exist \cite{pendry1992_transfer_matrix}, \cite[pp. 71--77]{nemec2006phd}, enabling to compute,  in frequency-domain, e.g. the reflection and transmission of structures discretized in a grid. For simplicity, we describe the one-dimensional method.
%% 
%% The method is on dividing the structure into a sequence of homogeneous layers. For each layer, a $2\times 2$ \textit{transfer} matrix is prepared that relates the $\mathbf E$ and $\mathbf H$ of the forward and backward propagating waves. If the $m$-th layer has a wave impedance $Z_m$, refractive index $N_m$ and thickness $d_m$, the transfer matrix $\mathbb M^{(m)}$ is given as
%% \begin{equation} \mathbb M^{(m)} := \left(\begin{array}{cc} \cos\delta & (i/\gamma)\sin\delta \\ i\gamma\sin\delta & \cos\delta \end{array}\right), \quad\text{ where }\gamma:=1/Z_m\text{ and }\delta := k~N_m d_m.\label{eq_tmm1}\end{equation}
%% Multiplication of such matrices gives the overall transfer matrix of the layered structure, 
%% \begin{equation} \mathbb M^{(tot)} \equiv \left(\begin{array}{cc} m_{11} & m_{12} \\ m_{21} & m_{22} \end{array}\right) = \ldots \cdot \mathbb M^{(2)} \cdot \mathbb M^{(1)}. \label{eq_tmm2}\end{equation}
%% The overall reflection $r^{(tot)}$ and transmission $t^{(tot)}$ are then 
%% \begin{equation} r^{(tot)} = \frac{m_{11} + m_{12} - m_{21} - m_{22}}{m_{11} + m_{12} + m_{21} + m_{22}}, \quad\quad t^{(tot)}= \frac{2}{m_{11} + m_{12} + m_{21} + m_{22}}, \label{eq_rt_tmm}\end{equation}
%% if perpendicular only incidence is assumed and if the surrounding medium consists of air.
%% 
%% The TMM is instrumental not only for its obvious simplicity, but also for providing mathematical interpretation of observed phenomena and allowing to define arbitrary properties of the layers (whereas both FDTD and PWEM restrict e.g. the constituent permittivity to be positive).
%% }
%% %}}}


%% \subsection{Simulation of refraction on a wedge} % ... shall I write this?
%% \mdf{
%% \paragraph{Simulation setup}
%% \paragraph{Derivation of the beam deflection angle}
%% \paragraph{Why the beam deflection angle depends on beam direction}
%% \paragraph{Analysis of spatio-temporal spectrum}
%% \paragraph{Limitations of this method}
%% }

