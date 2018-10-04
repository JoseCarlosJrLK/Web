<template>
  <div id=''>
    
    <table class="table">
      <thead>
          <th>Teste</th>
      </thead>
      <tbody>
        <tr v-for="quest in lista">
          <td>{{ quest.perguntas }}</td>
        </tr>
      </tbody>
    </table>

  </div>
</template>

<script>
  export default {
    data(){
      return {
        lista:[]
      }
    },
    mounted(){
      this.$http.get('questionario.html').then( (req) => this.lista = req.data)
    }
  }
</script>

<style></style>
