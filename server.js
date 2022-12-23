const express=require('express');
const cors=require('cors');
const cookieSession=require('cookie-session');


const app=express();

var corsOptions={
    origin:'http://localhost:8081'
};

app.use(cors(corsOptions));

app.use(express.json());

app.use(express.urlencoded({extended:true}));

app.use(
    cookieSession({
        name:'attachment-session',
        secret:'COOKIE_SECRET',
        httpOnly:true
    })
)
const db=require('./app/models');
const dbConfig = require('./app/config/db.config');
const Role=db.role;

db.mongoose.connect(`mongodb://${dbConfig.HOST}:${dbConfig.PORT}/${dbConfig.DB}`,{
    useNewUrlParser:true,
    useUnifiedTopology:true
}
)
.then(()=>{
    console.log('Successfully connected to mongodb');
    initial();
})
.catch(err=>{
    console.error('connection error',err);
    process.exit();
})

function initial() {
    Role.estimatedDocumentCount((err, count) => {
      if (!err && count === 0) {
        new Role({
          name: "user"
        }).save(err => {
          if (err) {
            console.log("error", err);
          }
  
          console.log("added 'user' to roles collection");
        });
  
        new Role({
          name: "student"
        }).save(err => {
          if (err) {
            console.log("error", err);
          }
  
          console.log("added 'student' to roles collection");
        });
  
        new Role({
          name: "supervisor"
        }).save(err => {
          if (err) {
            console.log("error", err);
          }
  
          console.log("added 'supervisor' to roles collection");
        });
        new Role({
            name: "employer"
          }).save(err => {
            if (err) {
              console.log("error", err);
            }
    
            console.log("added 'employer' to roles collection");
          });
      }
    });
  }

app.get('/',(req,res)=>{
    res.json({message:'Welcome to the system'})
})

require('./app/routes/auth.routes')(app);
require('./app/routes/user.routes')

const PORT=process.env.PORT ||8080;
app.listen(PORT,()=>{
    console.log(`Server is running on port ${PORT}.`)
})