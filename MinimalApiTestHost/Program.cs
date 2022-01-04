using System.Net;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();
app.MapGet("/", () => $"Hello, World! v1.0: {Dns.GetHostName()}");
app.Run("http://*:3000");
