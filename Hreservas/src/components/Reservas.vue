<template>
  <div id="Receptor_Habitacion">
    <div class="container_numero_habitacion">
      <h2>Información de la reserva</h2>
      
      <form v-on:submit.prevent="Reservar">
        
        <input type="text" v-model="reserva.cliente" placeholder=" Cedula CLiente " />
        <input type="text" v-model="reserva.habitacion" placeholder="Númeor Habitación" />
        
        <br />
        <button type="submit">Reservar</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Reserva",
  data: function () {
    return {
      reserva: {
        id_reserva: 0,
        cliente:"",
        habitacion:"",
      },
    };
  },
  methods: {
    Reservar: function () {
      var self = this;
      console.log("la habitacion es:" + self.reserva.cliente);
      var ruta =
        "https://hreservas.herokuapp.com/reserva" ;
      console.log("La ruta es:" + ruta);
      axios
        .post(ruta,self.reserva)
        .then((result) => {
          alert("Cedula Cliente:"+ self.reserva.cliente+"\nNombre:"+self.reserva.habitacion+"\n Reservado! Acerquese al hotel y haga efectiva la reserva");
        })
        .catch((error) => {
          alert("Lo sentimos, la reserva no pudo llevarse a cabo")
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
