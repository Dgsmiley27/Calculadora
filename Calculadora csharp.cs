using System;
using System.IO;

namespace curso
{
    class Program
    {
        static void Main(string[] args)
        {

            Console.WriteLine("Qual operação vc quer fazer? = ");
            var operação = Console.ReadLine();
            if (operação =="soma")
          {
          Console.WriteLine("Escreva o primeiro numero");
          int n1 = int.Parse(Console.ReadLine());
          Console.WriteLine("Escreva o segundo numero");
          int n2 = int.Parse(Console.ReadLine());
          Console.WriteLine($"a soma entre{n1} e {n2} é igual a {n1+n2}");
          }
          if (operação =="subtração")
          {
            Console.WriteLine("Escreva o primeiro numero");
            int n1 = int.Parse(Console.ReadLine());
            Console.WriteLine("Escreva o segundo numero");
            int n2 = int.Parse(Console.ReadLine());
            Console.WriteLine($"a subtração entre {n1} e {n2} é igual a {n1-n2}");
          }
          if (operação =="divisão")
          {
            Console.WriteLine("Escreva o primeiro numero");
            int n1 = int.Parse(Console.ReadLine());
            Console.WriteLine("Escreva o segundo numero");
            int n2 = int.Parse(Console.ReadLine());
            Console.WriteLine($"a divisão entre {n1} e {n2} é igual a {n1/n2}");
          }
          if (operação =="multiplicação")
          {
            Console.WriteLine("Escreva o primeiro numero");
            int n1 = int.Parse(Console.ReadLine());
            Console.WriteLine("Escreva o segundo numero");
            int n2 = int.Parse(Console.ReadLine());
            Console.WriteLine($"a multiplicação entre {n1} e {n2} é igual a {n1*n2}");
          }
            
        }
    }
}
