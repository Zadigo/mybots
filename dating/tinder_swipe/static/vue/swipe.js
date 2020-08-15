var scoreperson = {
    template: "\
    <div>\
        <button @click='toggle(i)' v-for='(button, i) in buttons' :class='button.color'>{{ button.id }}</button>\
    </div>\
    ",
    data() {
        return {
            buttons: [
                {id: 1, color: "btn red darken-1", selected: false},
                {id: 2, color: "btn green darken-2", selected: false},
                {id: 3, color: "btn green darken-4", selected: false}
            ]
        }
    },
    methods: {
        toggle: function(index) {
            this.$data.buttons.forEach(button => {
                button.selected = false
            })
            this.$data.buttons[index].selected = !this.$data.buttons[index].selected
        }
    },
    computed: {
        selectedbutton() {
            return this.$data.buttons.filter(button => {
                return button.selected === true
            })
        }
    }
}

var matchperson = {
    template: "\
    <div>\
        <button @click='toggle(i)' v-for='(button, i) in buttons' :class='button.color'>{{ button.id }}</button>\
    </div>\
    ",
    data() {
        return {
            buttons: [
                {id: "yes", color: "btn greed darken-1", selected: false},
                {id: "no", color: "btn red darken-1", selected: false},
            ]
        }
    },
    methods: {
        toggle: function(index) {
            this.$data.buttons.forEach(button => {
                button.selected = false
            })
            this.$data.buttons[index].selected = !this.$data.buttons[index].selected
        }
    },
    computed: {
        selectedbutton() {
            return this.$data.buttons.filter(button => {
                return button.selected === true
            })
        }
    }
}

var card = {
    props: ["currentimage"],
    template: "\
    <div class='card'>\
        <div class='card-image'>\
            <img :src='item' alt='' class='responsive-img'>\
        </div>\
    </div>\
    ",
    data() {
        return {
            item: undefined
        }
    },
    mounted() {
        var self = this
        var url = "/get-image/" + self.$props.currentimage.toString()
        console.log(url)
        $.ajax({
            type: "GET",
            url: url,
            dataType: "json",
            success: function (response) {
                self.$data.item = response
            }
        });
    }
}

var app = new Vue({
    el: "#app",
    components: {card, scoreperson, matchperson},
    data() {
        return {
            images: [],
            currentimage: ""
        }
    },
    beforeMount() {
        var self = this
        $.ajax({
            type: "GET",
            url: "/get-images",
            dataType: "json",
            success: function (response) {
                self.$data.images = response["images"]
                self.$data.currentimage = self.$data.images.pop(0)
            }
        });
    }
})