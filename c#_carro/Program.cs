using System.Security.AccessControl;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace c#_carro
{
    public class Program
    {
        static void Main(string[] args)
        {
            
            /*criando um objeto*/

            Carro corsa = new Carro();
            corsa.Modelo = "Corsa";
            corsa.Marca = "Chevrolet";
            corsa.Chassi = "ABC123";
            corsa.Fabricante = "Chevrolet";
            corsa.Ligar();
            corsa.Acelerar();
            corsa.Frear();
            corsa.Desligar();
            Console.WriteLine("Nome do carro: " + corsa.Modelo);

            Carro gol = new Carro();
            gol.Modelo = "Gol";
            gol.Marca = "Volkswagen";
            gol.Chassi = "DEF456";
            gol.Fabricante = "Volkswagen";
            gol.Ligar();
            gol.Acelerar();
            gol.Frear();
            gol.Desligar();
            Console.WriteLine("Nome do carro: " + gol.Modelo);
        }
    }
}