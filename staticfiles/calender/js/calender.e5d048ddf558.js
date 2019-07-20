  // initialize the calendar
  // ----------------------------------------------------------------

  $('#calendar').fullCalendar({
    customButtons: {
    myCustomButton: {
      text: 'Freie Notiz',
      click: function() {

        latest_notes_id++;
       Date.prototype.addHours= function(h){
            this.setHours(this.getHours()+h);
            return this;
            }
        var currentdate = new Date().setMinutes(00);
        var currentdate_end =new Date().addHours(1).setMinutes(00);

        event = {
        title: "Freie Notiz",
        id: "note_" + latest_notes_id,
        type: "",
        start: currentdate,
        end: currentdate_end,
        note: "",
        allDay: "False",
        save: "note"
        }

        $('#calendar').fullCalendar( 'renderEvent', event , true );
      }
    }
  },
    header: {
        right: 'prev,next,today,month,agendaWeek,myCustomButton'
        },
      buttonsIcons : {
       prev: 'left-single-arrow',
       next: 'right-single-arrow',
    },
      viewRender: function(view, element){

        if(view.name == 'agendaWeek') {

    } else if(view.name == 'month'){

    }
  },

    defaultView: (function (){ if($(window).width()<=768){
        return defaultView = 'agendaDay';} else { return defaultView = 'agendaWeek';}})(),

    slotLabelFormat: [
        'MMMM YYYY', // top level of text
        'HH:mm'        // lower level of text
    ],
    columnHeaderText: function(mom) {
    if (mom.weekday() === 0) {
      return 'Montag';}
      if (mom.weekday() === 1) {
      return 'Dienstag';}
      if (mom.weekday() === 2) {
      return 'Mittwoch';}
      if (mom.weekday() === 3) {
      return 'Donnerstag';}
      if (mom.weekday() === 4) {
      return 'Freitag';}
      if (mom.weekday() === 5) {
      return 'Samstag';}
      if (mom.weekday() === 6) {
      return 'Sonntag';}
     },
    allDaySlot: false,
    aspectRatio: 1,
    slotDuration: '00:30:00',
    minTime: '06:00:00',
    maxTime: '22:00:00',
    nowIndicator: true,
    eventTextColor: 'white',
    themeSystem: 'bootstrap4',
    height: "auto",
    contentHeight: "auto",
    events: events,
    eventColor:'#676b70',
    eventBackgroundColor: '#343a40',
    timeFormat: 'H(:mm)',
    weekNumbers: true,
    color: 'white',
    firstDay: 1,
    textColor: 'white',
    editable: true,
    eventLimit: true,
    handleWindowResize: true,
    droppable: true,

    eventRender: function(event, element, view) {
            element.attr("id","pop_" + event._id);

                if (event.save=="note"){
                    element.css({"border-left": "5px solid #2de2a0"});
                    }
                else {
                var colors = ['#1abc9c', '#2ecc71', '#3498db', '#9b59b6', '#34495e', '#f1c40f', '#e67e22', '#e74c3c', '#95a5a6', '#34495e', '#f1c40f', '#e67e22', '#e74c3c', '#95a5a6',];
                var color = colors[event.type];


                element.css({"border-left": "5px solid #20749b"});

                if (event.note != "") {
                        element.find(".fc-content").prepend("<div class='note_icon_cont'><span class='glyphicon glyphicon-flag' id='note_icon'></span></div>");
                        }
                }

            if (view.name == 'listDay') {
                element.find(".fc-list-item-time").append("<span class='closeon'>&times;</span>");

            } else {
                element.find(".fc-content").prepend("<span class='closeon'>&times;</span>");
            }

            element.find(".closeon").on('click', function () {
                deleteMyData(event);
                $('#calendar').fullCalendar('removeEvents', event._id);
            });

            element.popover({
                    html: true,
                    animation: false,
                    title: "" + event.title + "",
                    trigger: "click",
                    content: "<div style='color: white;' id= '" + event._id + "cont' >Notizen: <textarea class='form-control' id='" + event._id + "'>" + event.note + " </textarea><button style='margin-top: 10px; margin-bottom: 10px; float: right;' type='button' id='pop_save' onclick='save_note(this)' class='btn btn-primary'>Speichern</button></div",
                    });
    },

    eventReceive: function(event) {
            console.log("Recieve")
            latest_id++;
            event.id = latest_id;
            event.note = "";
            event.save = "event";
            $('#calendar').fullCalendar('updateEvent', event);
            saveMyData(event);

            },

    eventDrop: function (event, delta, revertFunc, jsEvent, ui, view) {
                $('.popover').popover('hide');
                saveMyData(event);
           },

    eventResize: function (event, delta, revertFunc, jsEvent, ui, view) {
                 saveMyData(event);
             },
    eventAfterAllRender: function (view) {

                    var currentDate = $('#calendar').fullCalendar('getDate');
                    var currentYear = currentDate._i[0]
                    $.ajax({
                        url:"https://feiertage-api.de/api/?jahr="+ currentYear +"&nur_land=SH",
                        type: "GET",
                        success: function (data) {
                        console.log(data);
                        var holidays = []
                        for (var f in data){
                            var holiday_form = moment(data[f].datum,'YYYY-MM-DD');
                            holidays.push([holiday_form, f]);
                        };

				        var holidayMoment = [];

				        for(var i = 0; i < holidays.length; i++) {
					        holidayMoment = holidays[i][0];
					        if (view.name == 'month') {
						        $("td[data-date=" + holidayMoment.format('YYYY-MM-DD') + "]").addClass('holiday');
						        var holiday_name = $("td[data-date=" + holidayMoment.format('YYYY-MM-DD') + "]")

                                check_month = holiday_name.find("span").text();
                                if (check_month != holidays[i][1]){
                                    holiday_name.find("span").text(holidays[i][1]);
                                }

					        } else if (view.name =='agendaWeek') {
					            $(".fc-event .fc-bg").css('background-color','#343a40');
					        	var days = ['Sonntag', 'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag'];
                                var d = new Date(holidayMoment);
						        var classNames =  $("th[data-date="+holidayMoment.format('YYYY-MM-DD')+"]").addClass('holiday');
                                var holiday_name = $("th[data-date="+holidayMoment.format('YYYY-MM-DD')+"]");
                                check_week = holiday_name.find("span").text();
                                if (check_week != holidays[i][1]){
                                    holiday_name.find("span").text(holidays[i][1]);
                                }

					        } else if (view.name == 'agendaDay') {
						        if(holidayMoment.format('YYYY-MM-DD') == $('#calendar').fullCalendar('getDate').format('YYYY-MM-DD')) {
							        $("td.fc-col0").addClass('holiday');
						            };
					            }
				            }
                        }
                    });
	}
  });



function save_note(ev){
    console.log(ev.parentElement.id.replace(/cont/g,''));
    var id = ev.parentElement.id.replace(/cont/g,'')
    var event = $('#calendar').fullCalendar( 'clientEvents' , id )[0];
    console.log(event.save);

                    if (event.save=="event"){
                    var txt = $('#' + event._id).val();
                    event.note = txt;
                    saveMyData(event);


                }else if(event.save=="note"){
                    var txt = $('#' + event._id).val();
                    console.log(event);
                    event.title = txt;
                    saveMyData(event);
                    }

                if(typeof txt != "undefined")
                {
                    $('#calendar').fullCalendar('removeEvents', event._id);
                    $('#calendar').fullCalendar( 'renderEvent', event, true );
                    $('.popover').popover('hide');
                };
}
document.getElementByClassName("fc-myCustomButton-button btn btn-primary").dataset.target = "modal";
document.getElementByClass("fc-myCustomButton-button btn btn-primary").dataset.target = "modal";

console.log(document.getElementByClassName("fc-myCustomButton-button btn btn-primary"));
