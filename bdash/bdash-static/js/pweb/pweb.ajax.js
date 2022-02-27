PWeb.ajax = (function(){

    return{

        call: function(settings){
           var defaults = {
               url:null,
               method:"POST",
               dataType:"json",
               afterComplete:null,
               beforeSubmit:null,
               success:null,
               beforeSend:undefined,
               complete:undefined,
               data:null
           }

            if(settings){
                jQuery.extend(defaults, settings);
            }

            jQuery.ajax({
                url:defaults.url,
                type:defaults.method,
                dataType:defaults.dataType,
                data: defaults.data,
                beforeSend:function(){
                    if(defaults.beforeSend !== undefined){
                        defaults.beforeSend();
                    }
                },

                success:function(content){
                   defaults.success(content);
                },

                complete:function(){
                    if(defaults.complete !== undefined){
                        defaults.complete();
                    }
                }
            });
        }
    }
}());