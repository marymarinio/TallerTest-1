using System;

namespace Patron_decorator
{
    internal class Program
    {
        static void Main(string[] args)
        {
            ComidaRapidaComponente pollo = new PolloBroaster();
            pollo = new Gaseosa(pollo, Tamanio.Mediano, TipoGaseosa.CocaCola);
            pollo = new PapasFritas(pollo, Tamanio.Grande);
            Console.WriteLine($"Producto: {pollo.Descripcion}\nCosto Total: {pollo.Costo}bs.");
        }
    }
}
