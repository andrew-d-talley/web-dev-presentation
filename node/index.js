const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const axios = require('axios').default;

const app = express();
app.use(bodyParser.json());
app.use(cors());

const port = 8080;

app.post('/recommendations', async (req, res) => {
  try {
    console.log("Asking for recommendation to Python");
    const {data} = await axios.post('http://localhost:5000/recommendations', {
      in_cart: req.body.in_cart
    });
    console.log("Received recommendations: ", data, "\n");
    res.send(data);
  } catch (err) {
    console.error(err);
    res.status(500).send();
  }
});

app.listen(port, () => {
  console.log(`Listening at http://localhost:${port}`);
});