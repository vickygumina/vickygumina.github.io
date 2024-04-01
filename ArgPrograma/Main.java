import java.util.*;

class jugador {
    String nombre;
    int ptoAtaque;
    int ptoDefensa;

    public jugador(String nombre, int ptoAtaque, int ptoDefensa) {
        this.nombre = nombre;
        this.ptoAtaque = ptoAtaque;
        this.ptoDefensa = ptoDefensa;
    }
}

class Main {
    static List<jugador> mjAtacantes;
    static List<jugador> mjDefensores;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();

        for (int t = 1; t <= T; t++) {

            List<jugador> equipo = new ArrayList<>();

            for (int i = 0; i < 10; i++) {
                String nombre = scanner.next();
                int ptoAtaque = scanner.nextInt();
                int ptoDefensa = scanner.nextInt();
                equipo.add(new jugador(nombre, ptoAtaque, ptoDefensa));
            }

            mjAtacantes = new ArrayList<>();
            mjDefensores = new ArrayList<>();
            
            equipo.sort((jugador1, jugador2) -> {
                // Comparamos por orden lexicográfico del nombre
                return jugador1.nombre.compareTo(jugador2.nombre);
            });

            equipo.sort((jugador1, jugador2) -> {
                // Comparamos por puntaje de defensa en orden descendente
                return Integer.compare(jugador2.ptoDefensa, jugador1.ptoDefensa);
            });

            equipo.sort((jugador1, jugador2) -> {
                // Comparamos por puntaje de ataque en orden descendente
                int comparacionAtaque = Integer.compare(jugador2.ptoAtaque, jugador1.ptoAtaque);
                if (comparacionAtaque != 0) {
                    return comparacionAtaque; // Si los puntajes de ataque son diferentes, retornamos la comparación
                } else {
                    // Si los puntajes de ataque son iguales, comparamos por puntaje de defensa
                    return Integer.compare(jugador1.ptoDefensa, jugador2.ptoDefensa);
                }
            });
                
            mjAtacantes.addAll(equipo.subList(0, 5));
            mjDefensores.addAll(equipo.subList(5, 10));

            List <String> nombreAtacante = new ArrayList<>();

            for(jugador jugador : mjAtacantes){
                nombreAtacante.add(jugador.nombre);

            }

            Collections.sort(nombreAtacante);

            List <String> nombreDefensores = new ArrayList<>();

            for(jugador jugador : mjDefensores){
                nombreDefensores.add(jugador.nombre);

            }

            Collections.sort(nombreDefensores);

            System.out.println("Case " + t + ":");
            System.out.print("(");

            for (int i = 0; i < 5; i++) {
                System.out.print(nombreAtacante.get(i));
                if (i < 4) {
                    System.out.print(", ");
                }
            }

            System.out.println(")");
            System.out.print("(");

            for (int i = 0; i < 5; i++) {
                System.out.print(nombreDefensores.get(i));
                if (i < 4) {
                    System.out.print(", ");
                }
            }
            System.out.println(")");
        }
        scanner.close();
    }

}