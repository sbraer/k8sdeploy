using System.Net;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();
app.MapGet("/", () => $"Hello, World! v1.0: {GetHostName()}");
app.Run("http://*:3000");

static string GetHostName()
{
    try
    {
        return Dns.GetHostName();
    }
    catch(Exception ex)
    {
        return ex.Message;
    }
}