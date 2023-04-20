using ContosoPizza7.Models;
using ContosoPizza7.Services;
using Microsoft.AspNetCore.Mvc;

namespace ContosoPizza7.Controllers;

[ApiController]
[Route("[controller]")]
public class PizzaController : ControllerBase
{
    public PizzaController()
    {
    }


// GET all action - витягти всі дані
[HttpGet]
public ActionResult<List<Pizza>> GetAll() =>
PizzaService.GetAll();

// GET by Id action - витягти дані за id
[HttpGet("{id}")]
public ActionResult<Pizza> Get(int id)
{
    var pizza = PizzaService.Get(id);

    if(pizza == null)
        return NotFound();

    return pizza;
}

// POST action - створити
[HttpPost]
public IActionResult Create(Pizza pizza)
{            
    PizzaService.Add(pizza);
    return CreatedAtAction(nameof(Get), new { id = pizza.Id }, pizza);
}

// PUT action - оновити/редагувати за id
[HttpPut("{id}")]
public IActionResult Update(int id, Pizza pizza)
{
    if (id != pizza.Id)
        return BadRequest();
           
    var existingPizza = PizzaService.Get(id);
    if(existingPizza is null)
        return NotFound();
   
    PizzaService.Update(pizza);           
   
    return NoContent();
}

// DELETE action - видалити за id
[HttpDelete("{id}")]
public IActionResult Delete(int id)
{
    var pizza = PizzaService.Get(id);
   
    if (pizza is null)
        return NotFound();
       
    PizzaService.Delete(id);
   
    return NoContent();
}

}