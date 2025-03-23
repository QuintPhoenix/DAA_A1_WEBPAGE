import streamlit as st
from streamlit_option_menu import option_menu

# Create the sidebar navigation menu
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Readme", "Dataset Exploration", "Tomita", "ELS", "Chiba"],
        #icons=["file-text", "geo-alt", "map", "lightning"],  # Optional: Bootstrap icons
        menu_icon="list",  # Optional: Menu icon
        default_index=0,  # Default selected index
    )

# Display content based on selection
if selected == "Readme":
    st.title("Readme")
    st.write(
        "A maximal clique is a complete subgraph (where every pair of vertices is connected by an edge) that cannot be extended by including any additional vertex. Finding all maximal cliques in a graph is a fundamental problem in graph theory with applications in social network analysis, bioinformatics, document clustering, and e-commerce.")

    st.write(
        "The problem of listing all maximal cliques is challenging because the number of maximal cliques can be exponential in the worst case. However, many real-world graphs are sparse, meaning they have relatively few edges compared to the maximum possible number. This sparsity can be measured using a graph parameter called degeneracy.")

    st.write("This application implements three different algorithms for finding all maximal cliques:")
    st.write("1. The ELS algorithm (Eppstein, Löffler, and Strash)")
    st.write("2. The Tomita algorithm")
    st.write("3. The Chiba-Nishizeki algorithm")

elif selected=="Dataset Exploration":
    st.title("Dataset Exploration")
    st.header("Dataset 1: Email-Enron")
    st.write("The network models email interactions within Enron, where nodes represent individual email addresses and edges signify that at least one email was exchanged between them. Its high clustering coefficient reflects dense local connections, making it a useful dataset for analyzing communication structures within organizations. Researchers can leverage it to uncover patterns like tightly connected groups or clusters.")
    st.write("No. of Nodes = 36692")
    st.write("No. of Edges = 183,831")
    st.image("Email-enron_dataset.png", caption="Dataset-1", use_container_width=True)

    st.header("Dataset 2: as-Skitter")
    st.write("The Skitter Internet Topology Dataset is a comprehensive dataset that maps the structure of the internet as a graph. ")
    st.write("No. of Nodes = 1696415")
    st.write("No. of Edges = 11095298")
    st.image("as-Skitter_dataset.png", caption="Dataset-2", use_container_width=True)
    
    st.header("Dataset 3: Wiki-vote")
    st.write("This dataset captures voting behavior in Wikipedia administrator elections, where connections indicate votes cast between users. Due to its relatively low clustering coefficient, it exhibits weaker local connectivity. It serves as a valuable resource for studying social dynamics and decision-making within online communities.")
    st.write("No. of Nodes = 7115")
    st.write("No. of Edges = 103,689")
    st.image("Wiki-vote_dataset.png", caption="Dataset-3", use_container_width=True)


elif selected == "Tomita":
    st.title("Tomita Algorithm")

    st.write(
        "The Tomita algorithm is a depth-first search approach for generating all maximal cliques of an undirected graph. Key features:")
    st.write("- Uses a pivoting strategy to reduce the number of recursive calls")
    st.write("- Achieves optimal worst-case time complexity of O(3^(n/3)) for an n-vertex graph")
    st.write("- Prints maximal cliques in a tree-like form to save space")

    st.header("Algorithm Overview")
    st.write("1. Maintains a set Q of vertices that form a complete subgraph")
    st.write("2. Recursively expands Q by adding vertices from the common neighborhood")
    st.write("3. Uses pivoting: chooses a vertex u that maximizes |CAND ∩ Γ(u)| to minimize branching")
    st.write("4. Outputs maximal cliques when no further expansion is possible")

    st.header("Time Complexity")
    st.write("- O(3^(n/3)) for an n-vertex graph")
    st.write("- This is optimal since there can be up to 3^(n/3) maximal cliques in an n-vertex graph")

    st.header("Practical Performance")
    st.write("- Very fast in practice, especially for dense graphs")
    st.write("- Outperforms other algorithms in most benchmark tests")
    st.write("- Requires less memory than algorithms that list all cliques directly")

    st.code('''
    procedure CLIQUES(G)
        /* Graph G= (V,E) */
    begin
        /* global variable Q is to constitute a clique */
        EXPAND(V,V)
    end of CLIQUES

    procedure EXPAND(SUBG, CAND)
    begin
        if SUBG=∅
            then print ("clique,")
                /* to represent that Q is a maximal clique */
            else u:= a vertex u in SUBG that maximizes |CAND∩Γ(u)|;
                while CAND - Γ(u)≠∅
                    do q:= a vertex in (CAND - Γ(u));
                        print (q,",");
                        SUBGq:=SUBG∩Γ(q)
                        CANDq:= CAND∩Γ(q);
                        EXPAND(SUBGq,CANDq)
                        CAND:=CAND - {q};
                        print ("back,");
                    od
            fi
    end of EXPAND
    ''', language='pascal')
    st.write("Run Time Comparision b/w all three Datasets:")
    st.write("Time Histogram:")
    st.image("images/tomita_time.png")

elif selected == "Chiba":
    st.title("Chiba-Nishizeki Algorithm")

    st.write(
        "The Chiba-Nishizeki algorithm is designed for finding maximal cliques in sparse graphs, with running time expressed in terms of the arboricity of the graph.")

    st.header("Key Concepts")
    st.write("- Arboricity (a(G)): The minimum number of edge-disjoint spanning forests into which G can be decomposed")
    st.write("- For a graph with n vertices and m edges: a(G) ≤ [(2m+n)^(1/2)/2]")
    st.write("- For planar graphs: a(G) ≤ 3")

    st.header("Algorithm Strategy")
    st.write("- Vertices are initially ordered (typically by nondecreasing degree) and processed one at a time; after exploring all cliques that include a vertex, it is deleted to prevent duplicate clique generation.")
    st.write("- The algorithm builds cliques recursively by extending a candidate clique only with those vertices that are common neighbors to all members of the current clique.")
    st.write("- By analyzing the graph’s arboricity (a measure of its sparsity), the method limits the number of candidate extensions, which keeps the running time low in sparse graphs.")
    st.write("- Before outputting a clique, tests are performed to ensure it is maximal and that it is produced in a canonical (typically lexicographically largest) order, thereby eliminating redundancies.")

    st.header("Time Complexity")
    st.write("O(a(G)m) time per clique, where m is the number of edges")

    st.header("Space Complexity")
    st.write("O(m), where m is the number of edges")


    st.code('''
    procedure CLIQUE;
    procedure UPDATE (i, C);
        begin
            if i = n + 1 then
                print out a new clique C;
            else begin
                if C - N(i) ≠ ∅ then UPDATE(i + 1, C);
                {prepare for tests}
                {compute T[y] = |N(y) ∩ C ∩ N(i)| for y ∈ V - C - {i}}
                for each vertex x ∈ C ∩ N(i)
                    do for each vertex y ∈ N(x) - C - {i}
                        do T[y] := T[y] + 1;
                {compute S[y] = |N(y) ∩ (C - N(i))| for y ∈ V - C}
                for each vertex x ∈ C - N(i)
                    do for each vertex y ∈ N(x) - C
                        do S[y] := S[y] + 1;
                FLAG := true;
                {maximality test}
                if there exists a vertex y ∈ N(i) - C such that y < i and T[y] = |C ∩ N(i)|
                    then FLAG := false;
                {lexico. test}
                {C ∩ N(i) corresponds to C₀ in Lemma 6}
                sort all the vertices in C - N(i) in ascending order j₁ < j₂ < ... < jₚ, where p = |C - N(i)|;
                {case S(y) ≥ 1. See Lemma 6.}
                for k := 1 to p
                    do for each vertex y ∈ N(jₖ) - C such that y < i and T[y] = |C ∩ N(i)|
                        do if y ≥ jₖ then S[y] := S[y] - 1; 
                        else if (jₖ is the first vertex which satisfies y < jₖ)
                            then if (S[y] + k - 1 = p) and (y ≥ jₖ₋₁) then FLAG := false;
                {case S(y) = 0}
                if C ∩ N(i) ≠ ∅ then
                    for each vertex y ∉ C ⋃ {i} such that y < i, T[y] = |C ∩ N(i)|, and S[y] = 0
                        do if jₚ < y then FLAG := false;
                        else if jₚ < i - 1 then FLAG := false;
                {reinitialize S and T}
                for each vertex x ∈ C ∩ N(i)
                    do for each vertex y ∈ N(x) - C - {i}
                        do T[y] := 0;
                for each vertex x ∈ C - N(i)
                    do for each vertex y ∈ N(x) - C
                        do S[y] := 0;
                if FLAG then begin
                    SAVE := C - N(i);
                    C := (C ∩ N(i)) ⋃ {i};
                    UPDATE(i + 1, C);
                    C := (C - {i}) ⋃ SAVE;
                end;
            end;
        end;

    begin {of CLIQUE}
        number the vertices of a given graph G in such a way that d(1) ≤ d(2) ≤ ... ≤ d(n);
        for i := 1 to n {initialize S and T}
            do begin S[i] := 0; T[i] := 0; end;
        C := {1};
        UPDATE(2, C);
    end; {of CLIQUE};

    ''', language='pascal')
    st.write("Run Time Comparision b/w all three Datasets:")
    st.write("Time Histogram:")
    st.image("images/chiba_time.png")

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
    st.header("Dataset used here")
    st.write("dataset-1 = Email_Enron")
    st.write("dataset-2 = as-Skitter")
    st.write("dataset-3 = wiki-Vote")
    st.header("Dataset-1")
    st.write("Nodes = 36692, Undirected Edges = 183831")
    st.write( "Largest size Clique = 20")
    st.write("Total Number of Maximal Cliques: 226859")
    st.image("output2_histogram.png", caption="Dataset-1", use_container_width=True)
    st.header("Dataset-2")
    st.write("Nodes = 36692, Undirected Edges = 183831")
    st.write( "Largest size Clique = 67")
    st.write("Total Number of Maximal Cliques: 226859")
    st.image("clique_size_histogram.png", caption="Dataset-2", use_container_width=True)
    st.header("Dataset-3")
    st.write("Nodes = 36692, Undirected Edges = 183831")
    st.write( "Largest size Clique = 17")
    st.write("Total Number of Maximal Cliques: 226859")
    st.image("output3_histogram.png", caption="Dataset-3", use_container_width=True)
