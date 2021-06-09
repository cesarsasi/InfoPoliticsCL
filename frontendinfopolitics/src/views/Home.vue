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
    <v-btn @click="recopilar_data">

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
        {label: "Regiones",items:["Arica","Metropolitana","BioBio"],reference:"region",model:""},
      ],
    }
  },
  methods:{
    castear_region: function(){
      
    },
    recopilar_data: function(){
      this.result = "";
      for(let input of this.inputs){
        if(input.model.localeCompare("") != 0){
          this.result += input.reference + ":" + input.model;
        }
      }
      this.show = true;
    }
  }
}
</script>
