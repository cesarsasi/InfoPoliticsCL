<template>
  <v-card class="flex d-flex flex-column">
    <v-card-title primary-title>
      <h3 class="headline mb-0">{{ $showInfo(notice.title) }}</h3>
    </v-card-title>
    <v-card-text>
      <h3 class="body-1 pa-4">{{ $showExcerpt(notice.excerpt) }}</h3>
    </v-card-text>
    <v-divider></v-divider>
    <v-card-actions>
      <v-row>
        <v-col class="d-flex justify-start" align-self="center">
          <h2 class="headline text-center pl-2 pt-4 body-1">
            Fecha: {{ $showInfo(notice.date) }}
          </h2>
        </v-col>
        <v-col class="d-flex justify-start" align-self="center">
          <h2 class="headline text-center pl-2 pt-4 body-1">
            Fuente: Ciper Chile
          </h2>
        </v-col>
        <v-col class="d-flex justify-end" align-self="center">
          <v-btn
            class="text-right pr-2 body-1 blue--text lighten-1--text"
            text
            @click="goToDetail"
            >Ver más...</v-btn
          >
        </v-col>
      </v-row>
    </v-card-actions>
  </v-card>
</template>
<script>
export default {
  props: {
    notice: {
      type: Object,
      default: () => {},
    },
  },
  methods:{
    goToDetail: function(){
      this.$router.replace({name: "NewsDetail", params: {newDetail: this.notice}});
    }
  }
};
</script>
