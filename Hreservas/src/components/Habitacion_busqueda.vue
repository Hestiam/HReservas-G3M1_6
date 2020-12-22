<template>
  <div id="Receptor_Habitacion">
    <div class="container_numero_habitacion">
      <h2>Busqueda de Habitacion</h2>
      
      <form v-on:submit.prevent="procesarBusqueda">
        <input
          type="text"
          v-model="habitacion.habitacion_id"
          placeholder="304 - 305 - 306"
        />
        <br />
        <button type="submit">Buscar Habitación</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Habitacion_busqueda",
  data: function () {
    return {
      habitacion: {
        habitacion_id: "",
        camas: "",
        detalles: "",
      },
    };
  },
  methods: {
    procesarBusqueda: function () {
      var self = this;
      console.log("la habitacion es:" + self.habitacion.habitacion_id);
      var ruta =
        "http://127.0.0.1:8000/habitacion/" + self.habitacion.habitacion_id;
      console.log("La ruta es:" + ruta);
      axios
        .get(ruta)
        .then((result) => {
          alert("Número de camas:"+result.data.camas+"\nDetalles de la habitación: "+result.data.detalles);
        })
        .catch((error) => {
          if (error.response.status == "404")
            alert("ERROR 404: Habitación no encontrada.");
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