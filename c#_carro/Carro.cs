using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Carro
{
    public string Modelo;
    public string Marca;
    public string Chassi;
    public string Fabricante;

    /*crinado métodos - funções*/
    public void Ligar()
    {
        Console.WriteLine("Carro ligado!");
    }

    public void Desligar()
    {
        Console.WriteLine("Carro desligado!");
    }

    public void Acelerar()
    {
        Console.WriteLine("Carro acelerando...");
    }

    public void Frear()
    {
        Console.WriteLine("Carro freando...");
    }
}
