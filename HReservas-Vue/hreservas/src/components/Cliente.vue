<template>
  <div id="Cliente">
    <h2>
      Su nombre es: <span> {{ nombre }} </span>
    </h2>
    <h2>
      Su cedula es: <span> {{ cedula }} </span>
    </h2>
    <h2>
      Su email es: <span> {{ email }} </span>
    </h2>
  </div>
</template>


<script>
import axios from "axios";
export default {
  name: "Cliente",
  data: function () {
    return {
      nombre: "",
      cedula: "",
      email: ""
    };
  },
  created: function () {
    this.cedula = this.$route.params.cedula;
    let self = this;
    axios
      .get("http://127.0.0.1:8000/clientes/" + this.cedula)
      .then((result) => {
        self.cedula = result.data.cedula;
        self.nombre = result.data.nombre;
        self.email = result.data.email;
      })
      .catch((error) => {
        alert("ERROR Servidor");
      });
  },
};
</script>

<style>
#UserBalance{
width: 100%;
height: 100%;
display: flex;
flex-direction: column;
justify-content: center;
align-items: center;
}
#UserBalance h2{
font-size: 50px;
color: #283747;
}
#UserBalance span{
color: crimson;
font-weight: bold;
}
</style>
