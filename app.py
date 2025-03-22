import streamlit as st
from streamlit_option_menu import option_menu

# Create the sidebar navigation menu
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Readme", "Tomita", "Chiba", "ELS", "Results"],
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

elif selected == "Chiba":
    st.title("Chiba-Nishizeki Algorithm")

    st.write(
        "The Chiba-Nishizeki algorithm is designed for finding maximal cliques in sparse graphs, with running time expressed in terms of the arboricity of the graph.")

    st.header("Key Concepts")
    st.write("- Arboricity (a(G)): The minimum number of edge-disjoint spanning forests into which G can be decomposed")
    st.write("- For a graph with n vertices and m edges: a(G) ≤ [(2m+n)^(1/2)/2]")
    st.write("- For planar graphs: a(G) ≤ 3")

    st.header("Algorithm Strategy")
    st.write("1. Process vertices in non-increasing order of degree")
    st.write("2. For each vertex v, scan the edges in the subgraph induced by v's neighbors")
    st.write("3. Delete v after processing to avoid duplication")
    st.write("4. Uses the property that each triangle containing v corresponds to an edge joining two neighbors of v")

    st.header("Time Complexity")
    st.write("- O(a(G)m) time per clique, where m is the number of edges")
    st.write("- For planar graphs: O(n) time (linear)")
    st.write("- For general graphs: O(m^(3/2)) time in the worst case")

    st.header("Extensions")
    st.write("- Can be extended to find all complete subgraphs of order l in O(la(G)^(l-2)m) time")
    st.write("- Particularly efficient for sparse graphs with low arboricity")

    st.code('''
    procedure K3(G);
    {Let G be a graph with n vertices and m edges.}
    begin
        sort the vertices v₁, v₂,..., vₙ of G in such a way that d(v₁)≥d(v₂)≥...≥d(vₙ);
        for i:=1 to n-2
        do begin
            {find all the triangles containing vertex vᵢ, each of which corresponds
            to an edge joining two neighbors of vᵢ.}
            mark all the vertices adjacent to vᵢ;
            for each marked vertex u
            do begin
                for each vertex w adjacent to u
                do if w is marked
                    then print out triangle (vᵢ, u, w);
                erase the mark from u
            end;
            {delete vᵢ from G so that no duplication occurs.}
            delete vertex vᵢ from G and let G be the resulting graph
        end
    end;
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

    st.write("Test_Case1")
    st.write("Graph defined : n = 36692, m = 367662 ")
    st.write("Execution Time: 8394 ms")
    st.write("Total Number of Maximal Cliques: 226859")
    st.write("Clique Size Histogram:")
    st.image("output2_histogram.png")

    st.write("Test_Case2")
    st.write("Graph defined : n = 1696415, m = 11095298")
    st.write("Execution Time: ")
    st.write("Total Number of Maximal Cliques: ")
    st.write("Clique Size Histogram:")
    #st.image()

    st.write("Test_Case3")
    st.write("Graph defined : n = 7115, m = 103689")
    st.write("Execution Time: 9922 ms")
    st.write("Total Number of Maximal Cliques: 459002")
    st.write("Clique Size Histogram:")
    st.image("output3_histogram.png")


elif selected == "Results":
    st.title("Results")
    st.header("Datasets")
    st.write("dataset-1 = wiki-Vote")
    st.write("dataset-2 = Email_Enron")
    st.write("dataset-3 = as-Skitter")
    st.header("Dataset-1")
    st.write("Nodes = 36692, Undirected Edges = 183831")
    st.write("Execution Time: 109638 ms")
    st.write( "Largest size Clique = 20")
    st.write("Total Number of Maximal Cliques: 226859")
    st.image("images/wiki-Vote_histogram.png", caption="Dataset-1", use_container_width=True)
    st.image("images/email-Enron_histogram.png", caption="Dataset-2", use_container_width=True)
    st.image("images/as-Skitter_histogram.png", caption="Dataset-3", use_container_width= True)
