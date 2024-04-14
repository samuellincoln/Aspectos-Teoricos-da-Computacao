import java.util.HashMap;
import java.util.HashSet;

public class PATHProblem {
	class Edge {
		private String source, destination;
		public Edge (String source, String destination) {
			this.source = source;
			this.destination = destination;
		}
		public String getSource () {return this.source;}
		public String getDestination () {return this.destination;}
	}
	class Graph4PP {
		private String initialnode;
		private HashSet <Edge> edges;
		private HashMap <String, Boolean> marked;
		public Graph4PP (String initialnode, HashSet <Edge> edges) {
			this.initialnode = initialnode;
			this.edges = edges;
			HashMap <String, Boolean> markedlocal = new HashMap <String, Boolean> ();
			for (Edge e : this.edges) {
				markedlocal.put(e.getSource(), false);
				markedlocal.put(e.getDestination(), false);
			}
			markedlocal.put(initialnode, true);
			this.marked = markedlocal;
		}
		public boolean thereIsPath (String destination) {
			boolean noadditional = true;
			while (noadditional) {
				boolean aux = false;
				for (Edge e : this.edges) {
					if (this.marked.get(e.getSource())) {
						aux = aux || !this.marked.get(e.getDestination());
						this.marked.put(e.getDestination(), true);
					}
				}
				noadditional = aux;
			}
			return this.marked.get(destination);
		}
	}
	public static Graph4PP instGraph4PP (String source, HashSet <Edge> edges) {
		return (new PATHProblem ()).new Graph4PP (source, edges);
	}
	public static Edge instEdge (String source, String destination) {
		return (new PATHProblem ()).new Edge (source, destination);
	}
	public static void main (String [] args) {
		HashSet <Edge> edges = new HashSet <Edge> ();
		edges.add (instEdge ("A", "B"));
		edges.add (instEdge ("A", "C"));
		edges.add (instEdge ("A", "D"));
		edges.add (instEdge ("D", "E"));
		edges.add (instEdge ("F", "G"));
		Graph4PP g = instGraph4PP ("A", edges);
		System.out.println (g.thereIsPath("E"));
		System.out.println (g.thereIsPath("D"));
		System.out.println (g.thereIsPath("F"));
	}
}
