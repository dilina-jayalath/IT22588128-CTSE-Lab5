const express = require('express');
const app = express();
app.use(express.json()); // To parse JSON bodies

let items = ['Book', 'Laptop', 'Phone']; // In-memory list
const port = 8081;

// GET /items - Return all items
app.get('/items', (req, res) => {
    res.json(items);
});

// POST /items - Add a new item (expects { "name": "ItemName" })
app.post('/items', (req, res) => {
    const item = req.body.name;
    if (!item) {
        return res.status(400).send('Missing "name" in body');
    }
    items.push(item);
    res.status(201).send(`Item added: ${item}`);
});

// GET /items/{id} - Get item by index (ID)
app.get('/items/:id', (req, res) => {
    const id = parseInt(req.params.id);
    if (id < 0 || id >= items.length) {
        return res.status(404).send('Item not found');
    }
    res.send(items[id]);
});

app.listen(port, () => {
    console.log(`Item Service running on port ${port}`);
});