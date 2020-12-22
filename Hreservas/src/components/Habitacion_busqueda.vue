<template>
  <div id="UserTransaction">
    <div class="container_numero_reserva">
      <h2>Busqueda de Habitacion</h2>
      <form v-on:submit.prevent="procesarBusqueda">
        <input
          type="tetx"
          v-model="numero"
          placeholder="Ingresa el numero de tu habitación"
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
      habitacion_id: "none",
      camas: "none",
      detalles: "none",
    };
  },
  methods: {
    procesarBusqueda: function () {
      var info;
      var base="http://127.0.0.1:8000/habitacion/";
      let habit= this.data.habitacion_id;
      var ruta= base+habit;
      axios.get(ruta)
      .then(response =>{})
      .catch(e=>{})

    },
  },
};
</script>
    }
  }
};
</script>
<style>
</style>