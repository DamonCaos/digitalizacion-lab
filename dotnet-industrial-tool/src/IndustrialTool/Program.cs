using System;
using System.Data;
using System.Data.SqlClient;

namespace IndustrialTool
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== IndustrialTool · Digitalización ===");
            Console.WriteLine("Este es un esqueleto para utilidades internas de planta.\n");

            // TODO: sustituye por tu cadena de conexión real
            var connectionString = "Server=TU_SERVIDOR;Database=Produccion;User Id=USUARIO;Password=PASSWORD;";

            try
            {
                using (var connection = new SqlConnection(connectionString))
                {
                    connection.Open();
                    Console.WriteLine("Conexión SQL OK.");

                    var query = @"
                        SELECT TOP 10 FechaHora, Linea, Referencia, PiezasBuenas, PiezasScrap
                        FROM Produccion
                        ORDER BY FechaHora DESC";
                    
                    using (var command = new SqlCommand(query, connection))
                    using (var reader = command.ExecuteReader())
                    {
                        Console.WriteLine("\nÚltimos 10 registros de producción:");
                        while (reader.Read())
                        {
                            Console.WriteLine(
                                $"{reader["FechaHora"],19} | L{reader["Linea"],2} | Ref: {reader["Referencia"],10} | Buenas: {reader["PiezasBuenas"],5} | Scrap: {reader["PiezasScrap"],5}"
                            );
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error conectando a la base de datos:");
                Console.WriteLine(ex.Message);
            }

            Console.WriteLine("\nPulsa cualquier tecla para salir...");
            Console.ReadKey();
        }
    }
}