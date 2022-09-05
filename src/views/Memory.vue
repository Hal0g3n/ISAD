<template>
    <div class="Memory"> <transition name=fade mode=out-in>

        <!-- Getting Personal Information -->
        <v-container v-if="details==0" fill-height key="details">
            <h1>Details</h1>

            <v-row>
                <v-col cols=12>
                    <h2 class="subheading grey--text">Sex</h2>
                    <v-select
                        label="Select Your Sex"
                        item-text="sex"
                        item-value="val"
                        :items="[{sex: 'Male', val: 0}, {sex: 'Female', val: 1}]"
                        v-model="gender.val"
                        outlined/>
                </v-col>
            </v-row>

            <v-row>
                <v-col cols=12>
                    <h2 class="subheading grey--text">Birthday</h2>
                    
                    <v-menu
                        v-model="menu"
                        :close-on-content-click="false"
                        transition="scale-transition"
                        offset-y
                        min-width="auto"
                        >
                        
                        <template v-slot:activator="{ on, attrs }">
                            <v-text-field
                                v-model="date"
                                label="Birthday Date"
                                prepend-icon="mdi-calendar"
                                readonly
                                v-bind="attrs"
                                v-on="on"/>
                        </template>

                        <v-date-picker
                            :active-picker.sync="activePicker"
                            v-model="date"
                            :max="(new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10)"
                            min="1950-01-01"
                        ></v-date-picker>
                    </v-menu>

                </v-col>
            </v-row>

            <v-row><v-btn id="btn1" @click="details != 0 ? $emit('complete', 'CDT') : ++details">Submit</v-btn></v-row>;
        </v-container>

        <!-- Memory Test -->
        <v-container v-else key="memory">
            <h1>Memorise these 3 words</h1>
            
            <li v-for="word in api.words" :key="word">
                {{ word }}
            </li>
            <v-btn @click="click">Memorised</v-btn>

        </v-container>

    </transition> </div>
</template>

<script lang="ts">
import Vue from "vue";
import { API } from "@/model/Data";

export default Vue.extend({
    data: () => ({
        api: API.getInstance(),
        gender: {val: -1},
        details: 0,
        menu: false,
        date: null,
        activePicker: "YEAR",
    }),

    watch: {
        menu(val) {
            val && setTimeout(() => (this.activePicker = "YEAR"));
        }
    },

    methods: {
        click() {
            this.details = 2;
            this.$emit("complete", "CDT");
            console.log(this.date);
            console.log(this.gender.val);
        }
    }
});

</script>



<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.25s ease-out;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>