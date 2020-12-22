<template>
  <div id="Receptor_Habitacion">
    <div class="container_numero_habitacion">
      <h2>Registro de Clientes</h2>
      
      <form v-on:submit.prevent="RegistrarCliente">
        <input type="text" v-model="cliente.cedula" placeholder="Cedula " />
        <input type="text" v-model="cliente.nombre" placeholder=" Nombre " />
        <input type="text" v-model="cliente.email" placeholder="Email" />
        
        <br />
        <button type="submit">Registrar Cliente</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Cliente",
  data: function () {
    return {
      cliente: {
        cedula: "",
        nombre:"",
        email:"",
      },
    };
  },
  methods: {
    RegistrarCliente: function () {
      var self = this;
      console.log("la habitacion es:" + self.cliente.cedula);
      var ruta =
        "http://127.0.0.1:8000/clientes/nuevo_cliente" ;
      console.log("La ruta es:" + ruta);
      axios
        .post(ruta,self.cliente)
        .then((result) => {
          alert("Cedula:"+ self.cliente.cedula+"\nNombre:"+self.cliente.nombre+"\nEmail de contacto: "+self.cliente.email+"\n Registrado Exitosamente");
        })
        .catch((error) => {
          alert("Lo sentimos el cliente no pudo ser registrado")
        });
    },
  },
};
</script>
    }
  }
};
</script>
<style>
.Receptor_Habitacion{
margin: 0;
padding: 0%;
height: 100%;
width: 100%;
display: flex;
justify-content: center;
align-items: center;
}
.container_numero_habitacion {
border: 3px solid #283747;
border-radius: 10px;
width: 25%;
height: 60%;
display: flex;
flex-direction: column;
justify-content: center;
align-items: center;
}
.container_numero_habitacion h2{
color: #283747;
}
.container_numero_habitacion form{
width: 50%;
}
.container_numero_habitacion input{
height: 40px;
width: 100%;
box-sizing: border-box;
padding: 10px 20px;
margin: 5px 0;
border: 1px solid #283747;
}
.container_numero_habitacion button{
width: 100%;
height: 40px;
color: #E5E7E9;
background: #283747;
border: 1px solid #E5E7E9;
border-radius: 5px;
padding: 10px 25px;
margin: 5px 0;
}
.container_numero_habitacion button:hover{
color: #E5E7E9;
background: crimson;
border: 1px solid #283747;
}
</style>
