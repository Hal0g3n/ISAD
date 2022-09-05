<template>
    <div class="Memory"> <transition name=fade mode=out-in>

        <!-- Getting Personal Information -->
        <v-container v-if="details!=1" fill-height key="details">
            <h1>Details</h1>

            <v-row>
                <v-col cols=12>
                    <h2 class="subheading grey--text">Gender</h2>
                    <v-select
                        label="Select Your Gender"

                        item-text="sex"
                        item-value="val"
                        :items="[{sex: 'Male', val: 1}, {sex: 'Female', val: 2}]"
                        v-model="gender.val"

                        :rules="[(v) => !!v || 'Please Select a Gender']"
                        required

                        outlined>

                    </v-select>

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
                                
                                :rules="[(v) => !!v || 'Please Select a Date']"
                                required

                                v-bind="attrs"
                                v-on="on"/>
                        </template>

                        <v-date-picker
                            :active-picker.sync="activePicker"
                            v-model="date"
                            :max="(new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10)"
                        ></v-date-picker>
                    </v-menu>

                </v-col>
            </v-row>

            <v-row>
                <v-col cols=12>
                    <h2 class="subheading grey--text mb-5">Years of Education</h2>
                    <NumberInputSpinner
                        v-model="edu"
                        :min="0"
                        :max="100"
                        :integerOnly="true"
                        :rules="[(v) => !!v || 'Please Select a Gender']"
                        required

                        outlined/>

                </v-col>
            </v-row>

            <v-row><v-btn class="primary" style="margin-top:3vmin" id="btn1" @click="info">Submit</v-btn></v-row>;
        </v-container>

        <!-- Memory Test -->
        <v-container v-else key="memory">
            <h1>Memorise these 3 words</h1>
            
            <li v-for="word in api.words" :key="word">
                {{ word }}
            </li>
            <v-btn class="primary" style="margin-top:3vmin" @click="memorise">Done!</v-btn>

        </v-container>

    </transition> </div>
</template>

<script lang="ts">
import Vue from "vue";
import { API } from "@/model/Data";
import NumberInputSpinner from "vue-number-input-spinner";

export default Vue.extend({
    data: () => ({
        api: API.getInstance(),
        gender: {val: 0},
        edu: 0,
        details: 0,
        menu: false,
        date: null as unknown as string,
        activePicker: "YEAR",
    }),

    components: {NumberInputSpinner},

    watch: {
        menu(val) {
            val && setTimeout(() => (this.activePicker = "YEAR"));
        }
    },

    methods: {
        info() {
            if (this.gender.val == 0) return;

            // Input validation
            if (this.date == null) return;

            if (this.details == 2) this.memorise();
            else ++this.details;
        },

        memorise() {
            this.details = 2;

            // Updates the API data
            this.api.edu = this.edu;
            this.api.gender = this.gender.val - 1; // Shifted up by 1 for easier input validation

            // Retarded code to calculate age from bday
            var now = new Date();
            var bday = new Date(Date.parse(this.date));
            this.api.age = now.getFullYear() - bday.getFullYear();
            now.setFullYear(now.getFullYear() - this.api.age);
            if (now.valueOf() < bday.valueOf()) this.api.age -= 1;

            this.$emit("complete", "CDT");
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