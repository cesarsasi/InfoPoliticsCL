<template>
  <v-flex class="home pa-6 box">
    <v-row>
      <v-col cols="12">
        <v-alert type="error" v-if="alert">Debes ingresar algún campo</v-alert>
      </v-col>
      <v-col class="d-flex justify-center">
        <v-card class="px-16 pb-16 pt-4 justify-center" width="50rem">
          <h1 class="py-6 text-center">
            ¡Comienza a buscar políticos por el campo que prefieras!
          </h1>
          <v-row>
            <v-col cols="12" v-for="(input, index) in inputs" :key="index">
              <v-select
                clearable
                :items="input.items"
                :label="input.label"
                v-model="input.model"
                v-if="input.reference === 'region'"
              >
              </v-select>
              <v-text-field :label="input.label" v-model="input.model" v-else>
              </v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col class="d-flex justify-center">
              <v-btn @click="do_query"> Buscar </v-btn>
            </v-col>
            <v-col class="d-flex justify-end">
              <v-btn text class="text-right pr-2 body-1 blue--text lighten-4--text" href="/news">Todas las noticias</v-btn>
            </v-col>
          </v-row>
          
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col class="d-flex justify-center">
        <v-card width="70%">
          <v-row v-if="show">
            <v-col class="d-flex justify-center pt-8">
              <h3 class="display-1">Respuesta:</h3>
              <p class="display-1">
                Hay {{ totalResults }} resultados en {{ timeResponse }} ms.
              </p>
            </v-col>
          </v-row>
          <v-divider id="results"></v-divider>
          <v-row v-if="show">
            <v-col cols="12" v-for="casted in castedInfo" :key="casted.id">
              <Political :political="casted"></Political>
              <v-divider></v-divider>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-flex>
</template>

<style>
.box {
  background: url("../../public/chilito.jpg") fixed;
  background-size: cover;
  height: 100%;
}
</style>

<script>
// @ is an alias to /src
import axios from "axios";
import Political from "@/components/Political.vue";

export default {
  name: "Home",
  components: {
    Political,
  },
  data() {
    return {
      totalResults: 0,
      timeResponse: 0,
      result: null,
      castedInfo: [],
      show: false,
      alert: false,
      inputs: [
        { label: "Nombre (nombre, apellido, nombre completo)", reference: "nombre", model: "" },
        { label: "Comuna (Ej: Arica)", reference: "comuna", model: "" },
        { label: "Partido (Ej: UDI)", reference: "partido", model: "" },
        {
          label: "Regiones",
          items: this.$listRegiones,
          reference: "region",
          model: "",
        },
      ],
    };
  },
  methods: {
    castear_region: function (region) {
      let num_reg = -1;
      num_reg = Object.keys(this.$regiones).find(
        (key) => this.$regiones[key] === region
      );
      return num_reg;
    },
    castListToQuery: function () {
      this.result = this.result.join("%20AND%20");
    },
    recopilar_data: function () {
      this.result = [];
      for (let input of this.inputs) {
        if (input.model) {
          if (input.reference === "region") {
            let numRegion = this.castear_region(input.model);
            this.result.push(input.reference + ":" + numRegion);
          } else {
            this.result.push(input.reference + ":" + input.model);
          }
        }
      }
      this.castListToQuery();
    },
    do_query: function () {
      this.recopilar_data();
      if (!this.result) {
        this.alert = true;
        location.href = "#"
        return;
      }
      console.log(this.result);
      this.castedInfo = [];
      let start = Date.now();
      axios
        .get("http://localhost:4000/search/" + this.result)
        .then((response) => {
          this.castedInfo = this.$castData(response.data);
          console.log("CASTED INFO: ", this.castedInfo);
          this.totalResults = this.castedInfo.length;
          this.show = true;
          this.alert = false;
          location.href = "#results";
          this.timeResponse = Math.floor((Date.now() - start) % 1000);
        })
        .catch((e) => console.log(e));
    },
  },
};
</script>
