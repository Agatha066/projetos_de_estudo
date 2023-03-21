using Internal;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace c#_Banco
{
    public class Program
    {
        ContaCorrente contaDaAgatha = new ContaCorrente();

        contaDaAgatha.titular = "Agatha";
        contaDaAgatha.agencia = 0123;
        contaDaAgatha.conta = 028821;
        contaDaAgatha.saldo = 1200.00;

        Console.WriteLine("Titular: " + contaDaAgatha.titular);
        Console.WriteLine("Agencia: " + contaDaAgatha.agencia);
        Console.WriteLine("Conta: " + contaDaAgatha.conta);
        Console.WriteLine("Saldo: R$" + contaDaAgatha.saldo);

        contaDaAgatha.saldo +=200.00;

        Console.WriteLine("Saldo Novo: R$" + contaDaAgatha.titular);
        Console.ReadLine();
    }
}