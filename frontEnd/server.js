const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const app = express();
const port = process.env.PORT || 3000;

// Połączenie z bazą danych MongoDB
mongoose.connect('mongodb://localhost:27017/mydb', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Definicja schematu kolekcji użytkowników
const userSchema = new mongoose.Schema({
  username: String,
  email: String,
});

const User = mongoose.model('User', userSchema);

// Obsługa formularza
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.post('/addUser', async (req, res) => {
  const { username, email } = req.body;
  try {
    const newUser = await User.create({ username, email });
    res.send(`Użytkownik ${newUser.username} dodany do bazy danych!`);
  } catch (error) {
    res.status(500).send('Błąd podczas dodawania użytkownika.');
  }
});

app.listen(port, () => {
  console.log(`Aplikacja działa na porcie ${port}`);
});
