import java.util.ArrayList;

class Empleado {
    private static int contadorEmpleados = 0; 
    private int Cc;
    private String nombre;
    private double sueldo;

   
    public Empleado(String nombre, double sueldo) {
        this.id = ++contadorEmpleados; // Se incrementa el contador estático
        this.nombre = nombre;
        this.sueldo= sueldo;
    }

   
    public String obtenerInfo() {
        return "C.c: " + Cc + ", Nombre: " + nombre + ", Sueldo: $" + sueldo;
    }

    
    public static int obtenerTotalEmpleados() {
        return contadorEmpleados;
    }
}

// Clase Empresa para manejar empleados
class Empresa {
    private ArrayList<Empleado> listaEmpleados;

  
    public Empresa() {
        this.listaEmpleados = new ArrayList<>();
    }

    
    public void agregarEmpleado(String nombre, double sueldo) {
        Empleado nuevoEmpleado = new Empleado(nombre, sueldo);
        listaEmpleados.add(nuevoEmpleado);
    }

   
    public void mostrarEmpleados() {
        if (listaEmpleados.isEmpty()) {
            System.out.println("No hay empleados registrados.");
        } else {
            System.out.println("Lista de empleados:");
            for (Empleado e : listaEmpleados) {
                System.out.println(e.obtenerInfo());
            }
        }
    }

   
    public void mostrarTotalEmpleados() {
        System.out.println("Total de empleados creados: " + Empleado.obtenerTotalEmpleados());
    }
}

public class GestionEmpleados {
    public static void main(String[] args) {
        Empresa empresa = new Empresa();

        
        empresa.agregarEmpleado("Jas Alarcon", 2500);
        empresa.agregarEmpleado("Maryury Salazar", 2800);
        empresa.agregarEmpleado("Sergio Alarcon", 3000);

        empresa.mostrarEmpleados();

        empresa.mostrarTotalEmpleados();
    }
}