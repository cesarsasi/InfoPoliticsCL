<template>
  <v-flex class="home pa-6">
    <v-row>
      <v-col cols="6" v-for="(input,index) in inputs" :key="index">
        <v-text-field
          :label="input.label"
          v-model="input.model"
          >
        </v-text-field>
      </v-col>
      <v-col cols="6" v-for="(select,index) in selects" :key="index">
        <v-select
          :items=select.items
          :label=select.label
          v-model=select.model
        >
        </v-select>
      </v-col>
    </v-row>
    <v-btn @click="recopilar_data" >
      Buscar
    </v-btn>
    <h1 v-show="show">
      {{result}}
    </h1>
  </v-flex>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  components: {
  
  },
  data(){
    return{
      result: null,
      show: false,
      inputs:[
        {label: "Nombre",reference:"nombre" ,model:""},
        {label: "Comuna",reference:"comuna",model:""},
        {label: "Partido",reference:"partido", model:""},
      ],
      selects:[
        {label: "Regiones",items:
          [
          "XV Región de Arica y Parinacota","I Región de Tarapacá","II Región de Antofagasta",
          "III Región de Atacama","IV Región de Coquimbo","V Región de Valparaíso",
          "Región Metropolitana de Santiago","VI Libertador Bernardo O'Higgins",
          "VII Región del Maule","XVI Región de Ñuble","VIII Región del Biobío",
          "IX Región de La Araucanía","XIV Región de Los Ríos","X Región de Los Lagos",
          "XI Región de Aisén de General Carlos Ibáñez del Campo",
          "XII Región de Magallanes y Antártica Chilena"
          ]
        ,reference:"region",model:""},
      ],
    }
  },
  methods:{
    castear_region: function(){
      let num_reg=-1;
      switch (Regiones) {
        case "XV Región de Arica y Parinacota":
          num_reg=15;
          break;
        case "I Región de Tarapacá":
          num_reg=1;
          break;
        case "II Región de Antofagasta":
          num_reg=2;
          break;
        case "III Región de Atacama":
          num_reg=3;
          break;
        case "IV Región de Coquimbo":
          num_reg=4;
          break;
        case "V Región de Valparaíso":
          num_reg=5;
          break;
        case "Región Metropolitana de Santiago":
          num_reg=0;
          break;
        case "VI Libertador Bernardo O'Higgins":
          num_reg=6;
          break;
        case "VII Región del Maule":
          num_reg=7;
          break;
        case "XVI Región de Ñuble":
          num_reg=16;
          break;
        case "VIII Región del Biobío":
          num_reg=8;
          break;
        case "IX Región de La Araucanía":
          num_reg=9;
          break;
        case "XIV Región de Los Ríos":
          num_reg=14;
          break;
        case "X Región de Los Lagos":
          num_reg=10;
          break;
        case "XI Región de Aisén de General Carlos Ibáñez del Campo":
          num_reg=11;
          break;
        case "XII Región de Magallanes y Antártica Chilena":
          num_reg=12;
          break;
      }
    },
    recopilar_data: function(){
      this.result = "";
      
      for(let input of this.inputs){
        if(input.model.localeCompare("") != 0){
          this.result += input.reference + ":" + input.model+ "AND";
        }
      }

      this.show = true;
    }
  }
}
</script>
