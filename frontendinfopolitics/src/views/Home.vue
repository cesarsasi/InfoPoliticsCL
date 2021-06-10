<template>
  <v-flex class="home pa-6">
    <v-row>
      <v-col cols="6" v-for="(input,index) in inputs" :key="index">
        <v-select
          :items=input.items
          :label=input.label
          v-model=input.model
          v-if="input.reference == 'region'"
        >
        </v-select>
        <v-text-field
          :label="input.label"
          v-model="input.model"
          v-else
        >
        </v-text-field>
      </v-col>
    </v-row>
    <v-btn @click="do_query">
      Buscar
    </v-btn>
    <v-row>
      <v-col>
        <v-flex 
        class="pa-4"
        v-show="show"
        v-for="casted in castedInfo"
        :key="casted.id"
        >
          <v-card
            color="#e3e3e3"
          >
      <v-card-title>{{showInfo(casted.nombre)}}</v-card-title>
      <v-card-text>Partido: {{showInfo(casted.partido)}}</v-card-text>
      <v-card-text>Comuna: {{showInfo(casted.comuna)}}</v-card-text>
      <v-card-text>Region: {{showInfo(casted.region)}}</v-card-text>

    </v-card>
        </v-flex>
      </v-col>
    </v-row>
    
  </v-flex>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: 'Home',
  components: {
  
  },
  data(){
    return{
      result: null,
      info: "",
      castedInfo: [],
      show: false,
      inputs:[
        {label: "Nombre",reference:"nombre" ,model:""},
        {label: "Comuna",reference:"comuna",model:""},
        {label: "Partido",reference:"partido", model:""},
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
    castear_region: function(regiones){
      let num_reg=-1;
      switch (regiones) {
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
      return num_reg;
    },
    castListToQuery: function(){
      this.result = this.result.join("%20AND%20");
    },
    recopilar_data: function(){
      this.result = [];
      for(let input of this.inputs){
        if(input.model.localeCompare("") != 0){
          if(input.reference.localeCompare("region") == 0){
            let numRegion = this.castear_region(input.model);
            this.result.push(input.reference + ":" + numRegion);
          }
          else{
            this.result.push(input.reference + ":" + input.model);
          }
        }
      }
      this.castListToQuery();
    },
    do_query: function(){
      this.recopilar_data();
      //console.log(this.result);
      this.castedInfo = [];
      this.info = "";
      axios.get('http://localhost:4000/search/' + this.result)
      .then(response => {
        this.info = response.data;
        for(const result of this.info){
          this.castedInfo.push(JSON.parse(result.replace(/'/g, '"')));
        }
        //console.log(JSON.parse(this.info[0].replace(/'/g, '"')).nombre);
        //console.log(JSON.parse("{'name':['John'], 'age':30, 'city':'New York'}".replace(/'/g, '"')));
      }).catch(e => console.log(e));
      this.show = true;
    },
    showInfo: function(arr){
      let ret = "";
      for(const a of arr){
        ret += a.toString().toUpperCase();
      }
      return ret;
    }


  }
}
</script>
