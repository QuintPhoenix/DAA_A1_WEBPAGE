import streamlit as st
from streamlit_option_menu import option_menu

# Create the sidebar navigation menu
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Readme", "Dataset Exploration", "Algorithm 1:", "Algorithm 4:", "Results"],
        #icons=["file-text", "geo-alt", "map", "lightning"],  # Optional: Bootstrap icons
        menu_icon="list",  # Optional: Menu icon
        default_index=0,  # Default selected index
    )

# Display content based on selection
if selected == "Readme":
    st.header("GROUP 18")
    st.write('Kevin Shah\t\t2022A7PS0067H')
    st.write('Shubham Chauhan\t\t2022A7PS0130H')
    st.write('Y Sai Shashank\t\t2022A7PS0061H')
    st.write('Pulin Patel\t\t2022A7PS1539H')
    st.write('Tanish Patel\t\t2022A7PS0103H')
    st.title("Readme")
    st.write(
        "A maximal clique is a complete subgraph (where every pair of vertices is connected by an edge) that cannot be extended by including any additional vertex. Finding all maximal cliques in a graph is a fundamental problem in graph theory with applications in social network analysis, bioinformatics, document clustering, and e-commerce.")

    st.write(
        "The problem of listing all maximal cliques is challenging because the number of maximal cliques can be exponential in the worst case. However, many real-world graphs are sparse, meaning they have relatively few edges compared to the maximum possible number. This sparsity can be measured using a graph parameter called degeneracy.")

    st.write("This application implements three different algorithms for finding all maximal cliques:")
    st.write("Algorithm 1: Exact Densest Subgraph Discovery using Flow Network")
    st.write("Algorithm 4: Core-based exact")

elif selected=="Dataset Exploration":
    st.title("Dataset Exploration")
    st.header("Dataset 1: AS-733")
    st.write("The As-733 dataset represents an Internet Autonomous Systems (AS) topology, with 1,486 nodes and 3,172 edges, capturing how different systems are connected at the network layer.")
    st.write("No. of Nodes = 1486")
    st.write("No. of Edges = 3172")
    st.image(r"images\Screenshot 2025-04-28 213141.png", caption="Dataset-1", use_container_width=True)

    st.header("Dataset 2: Yeast")
    st.write("The Yeast dataset models a biological network, containing 1,116 proteins (vertices) and 2,148 interactions (edges), used to study functional modules; it has no 4, 5, or 6-cliques. ")
    st.write("No. of Nodes = 1116")
    st.write("No. of Edges = 2148")
    st.image(r"images\Screenshot 2025-04-28 213343.png", caption="Dataset-2", use_container_width=True)
    
    st.header("Dataset 3: Netscience")
    st.write("The Netscience dataset is a co-authorship network in network science research, containing 1,589 vertices and 2,742 edges. It captures collaborations between scientists, and is relatively small but features dense regions, making it useful for testing densest subgraph discovery over edges, triangles, and small cliques​.")
    st.write("No. of Nodes = 1589")
    st.write("No. of Edges = 2742")
    st.image(r"images\Screenshot 2025-04-28 213523.png", caption="Dataset-3", use_container_width=True)


elif selected == "Algorithm 1:":
    st.title("Algorithm 1: Exact Densest Subgraph Discovery using Flow Network")
    
    st.header("Algorithm Overview")
    st.write("Algorithm-1 is a classical exact approach to solve the densest subgraph discovery (DSD) problem through binary search combined with network flow techniques. The key idea is to transform the DSD problem into a sequence of decision problems:")
    st.write("- Is there a subgraph with density greater than a given threshold α?")
    st.write("This is answered by constructing a carefully designed flow network and solving a minimum s-t cut problem. If a cut separates a non-trivial subgraph with average degree greater than α, then the threshold is increased; otherwise, it is decreased.The process continues until convergence to the optimal density value within a pre-specified precision.")
    st.write("The flow network construction:")
    st.write("- Nodes include a source node sss, a sink node ttt, graph vertices, and auxiliary nodes representing partial cliques (for h-clique density).")
    st.write("- Edges and capacities are carefully defined so that a feasible minimum cut corresponds to a subgraph exceeding the guessed density α.")
    st.write("- Solving for minimum cut effectively reduces to a maximum flow problem.")
    st.write("This method guarantees exact identification of the densest subgraph under both edge-density and h-clique-density definitions.")

    st.header("Time Complexity")
    st.write("The worst-case time complexity is:")
    st.image(r"images\Screenshot 2025-04-28 215409.png", caption="Dataset-3", use_container_width=True)
    st.write("- n is the number of vertices")
    st.write("- d is the maximum degree of any vertex")
    st.write("- |Λ∣ denotes the number of (h-1)-clique instances in the graph.")
    
    
    st.code('''
    Algorithm 1: The algorithm: Exact

    Input:
        G(V, E), Ψ(VΨ, EΨ)
    Output:
        The CDS D(VD, ED)

    1  initialize l ← 0, u ← max degG(v, Ψ) for v ∈ V;
    2  initialize Λ ← all the instances of (h−1)-clique in G, D ← ∅;
    3  while u − l ≥ 1 / (n(n−1)) do
    4      α ← (l + u) / 2;
    5      VF ← {s} ∪ V ∪ Λ ∪ {t};   // build a flow network
    6      for each vertex v ∈ V do
    7          add an edge s → v with capacity degG(v, Ψ);
    8          add an edge v → t with capacity α |VΨ|;
    9      for each (h−1)-clique ψ ∈ Λ do
    10         for each vertex v ∈ ψ do
    11             add an edge ψ → v with capacity +∞;
    12     for each (h−1)-clique ψ ∈ Λ do
    13         for each vertex v ∈ V do
    14             if ψ and v form an h-clique then
    15                 add an edge v → ψ with capacity 1;
    16     find minimum st-cut (S, T) from the flow network F(VF, EF);
    17     if S = {s} then
    18         u ← α;
    19     else
    20         l ← α, D ← the subgraph induced by S \ {s};
    21 return D;

    ''', language='pascal')


    

elif selected == "Algorithm 4:":
    st.title("Algorithm 4:")

    st.header("Algorithm Overview")
    st.write("The core insight behind Algorithm-4 is that vertices with high clique-core numbers are more likely to be part of the densest regions of the graph. Instead of examining the entire graph exhaustively, the algorithm identifies the (kₘₐₓ, Ψ)-core, i.e., the subgraph where every vertex participates in at least kₘₐₓ​ h-cliques.")
    st.write("The algorithm proceeds in two stages:")
    st.write("- (k, Ψ)-Core Decomposition: Compute for each vertex the maximum number kkk such that it belongs to a (k, Ψ)-core. This involves iteratively removing vertices of lowest clique-degree and updating their neighbors degrees.")
    st.write("- Dense Subgraph Extraction: Identify and output the subgraph induced by vertices with the highest core number kₘₐₓ.")
   
    
    st.header("Time Complexity")
    st.image(r"images\Screenshot 2025-04-28 220946.png")
    st.write("The time complexity of Algorithm-4 is driven by two main factors:")
    st.write("- **h-Clique Enumeration:** Before decomposition, the algorithm must enumerate all possible h-cliques (or pattern instances) in the graph. The worst-case number of cliques for each vertex is related to the maximum vertex degree (d).")
    st.write("- **Core Decomposition Process:** The iterative removal of vertices and updating of their neighbors' clique-degrees during the core decomposition.")

    st.subheader("Worst-Case Time Complexity")
    st.write("The worst-case time complexity of Algorithm-4 is:")
    st.latex(r"O(n \cdot d^h + |E| \cdot d)")

    st.write("where:")
    st.write("- n = number of vertices")
    st.write("- d = maximum degree of any vertex")
    st.write("- h = the size of the clique being considered")
    st.write("- |E| = the number of edges in the graph")

    st.subheader("Practical Performance")
    st.write("However, practical performance is often much better because most real-world graphs are sparse, resulting in relatively few clique instances.")

    st.header("Space Complexity")
    st.write("O(m), where m is the number of edges")


    st.code('''
    Algorithm 4: The algorithm: CoreExact

    Input: 
        G(V, E), Ψ(VΨ, EΨ)
    Output: 
        The CDS D(VD, ED)

    1  perform core decomposition using Algorithm 3;
    2  locate the (k'', Ψ)-core using pruning criteria;
    3  initialize C ← ∅, D ← ∅, U ← ∅, l ← ρ'', u ← kmax;
    4  put all the connected components of (k'', Ψ)-core into C;
    5  for each connected component C(VC, EC) ∈ C do
    6      if l > k'' then
    7          C(VC, EC) ← C ∩ ([l], Ψ)-core;
    8      build a flow network F(VF, EF) by lines 5–15 of Algorithm 1;
    9      find minimum st-cut (S, T) from F(VF, EF);
    10     if S = ∅ then continue;
    11     while u - l ≥ 1 / (|VC|(|VC| − 1)) do
    12         α ← (l + u) / 2;
    13         build F(VF, EF) by lines 5–15 of Algorithm 1;
    14         find minimum st-cut (S, T) from F(VF, EF);
    15         if S = {s} then
    16             u ← α;
    17         else
    18             if α > [l] then
    19                 remove some vertices from C;
    20             l ← α;
    21             U ← S \ {s};
    22     if ρ(G[U], Ψ) > ρ(D, Ψ) then
    23         D ← G[U];
    24 return D;

    ''', language='pascal')

elif selected == "ELS":
    st.title("ELS Algorithm")

    st.write(
        "The ELS (Eppstein, Löffler, and Strash) algorithm is a modified version of the Bron-Kerbosch algorithm optimized for sparse graphs.")

    st.header("Key Innovations")
    st.write("1. Uses degeneracy ordering of vertices")
    st.write("2. Combines ordered vertex processing with pivoting")
    st.write("3. Achieves near-optimal time complexity parametrized by degeneracy")

    st.header("Algorithm Steps")
    st.write("1. Compute a degeneracy ordering of the graph")
    st.write("2. For each vertex v in this ordering:")
    st.write("   - Find all maximal cliques containing v but no earlier vertices")
    st.write("   - Use the Tomita pivoting strategy for recursive calls")

    st.header("Time Complexity")
    st.write("- O(dn3^(d/3)) time, where d is the degeneracy of the graph")
    st.write("- This matches the worst-case output size of (n-d)3^(d/3) maximal cliques")
    st.write("- Fixed-parameter tractable with respect to degeneracy")

    st.header("Advantages")
    st.write("- Significantly faster than previous approaches for sparse graphs")
    st.write("- Provides theoretical explanation for the empirical success of Bron-Kerbosch variants")
    st.write(
        "- Particularly effective for real-world networks (social networks, web graphs, protein-protein interaction networks)")

    st.header("Comparison with Other Algorithms")
    st.write("- Chiba-Nishizeki: O(d²n(n-d)3^(d/3)) time")
    st.write("- Modified Chiba-Nishizeki for d-degenerate graphs: O(nd^(d+1)) time")
    st.write("- Brute force enumeration: O(nd²2^d) time")

    st.code('''
    proc BronKerboschDegeneracy ((V, E))
        for each vertex vᵢ in a degeneracy ordering v₀, v₁, v₂, ... of (V, E) do
            P ← Γ(vᵢ) ∩ {vᵢ₊₁, ..., vₙ₋₁}
            X ← Γ(vᵢ) ∩ {v₀, ..., vᵢ₋₁}
            BronKerboschPivot (P, {vᵢ}, X)
        end for

    proc BronKerboschPivot ((P, R, X))
        if P ∪ X = ∅ then
            report R as a maximal clique
        end if
        choose a pivot u ∈ P ∪ X that maximizes |P ∩ Γ(u)|
        for each vertex v ∈ P \ Γ(u) do
            BronKerboschPivot ((P ∩ Γ(v), R ∪ {v}, X ∩ Γ(v)))
            P ← P \ {v}
            X ← X ∪ {v}
        end for
    ''', language='pascal')

    st.write("Run Time Comparision b/w all three Datasets:")
    st.write("Time Histogram:")
    st.image("images/bron_time.png")


elif selected == "Results":
    st.title("Results")
    st.header("Dataset-1 : Email_Enron")
    st.write("Nodes = 36692, Undirected Edges = 183831")
    st.write( "Largest size Clique = 20")
    st.write("Total Number of Maximal Cliques: 226859")
    st.image("images/email-Enron_histogram.png", caption="Dataset-1", use_container_width=True)
    st.header("Dataset-2 : as-Skitter")
    st.write("Nodes = 36692, Undirected Edges = 183831")
    st.write( "Largest size Clique = 67")
    st.write("Total Number of Maximal Cliques: 226859")
    st.image("images/as-Skitter_histogram.png", caption="Dataset-2", use_container_width=True)
    st.header("Dataset-3 : Wiki-Vote")
    st.write("Nodes = 36692, Undirected Edges = 183831")
    st.write( "Largest size Clique = 17")
    st.write("Total Number of Maximal Cliques: 226859")
    st.image("images/wiki-Vote_histogram.png", caption="Dataset-3", use_container_width=True)
