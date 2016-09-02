
# BASIC CANARY TRENDING
# for index in range(length):
#     if index != length - 1:
#         print results[index].get("id"), datetime.strptime(results[index].get('created_at'),
#                                                           '%a, %d %b %Y %H:%M:%S %Z')
#         if at_border:
#             border = border + resolution
#             at_border = False
#         if datetime.strptime(results[index].get('created_at'), '%a, %d %b %Y %H:%M:%S %Z') <= border:
#             analysis_list.append(results[index].get('status'))
#         else:
#             at_border = True
#             print analysis_list
#             status_list.append(self.trend_analyzer(threshold, analysis_list))
#             analysis_list = []
#             analysis_list.append(results[index].get('status'))
#     else:
#         analysis_list.append(results[index].get('status'))
#         status_list.append(self.trend_analyzer(threshold, analysis_list))




#   CANARY TREND CALL
# def get_trend(project_id, canary_id):
#     results = [{u'status': u'pass', u'created_at': u'Tue, 26 Jul 2016 19:08:38 GMT', u'failure_details': u'', u'id': 1},
#                {u'status': u'pass', u'created_at': u'Tue, 26 Jul 2016 19:38:38 GMT', u'failure_details': u'', u'id': 2},
#                {u'status': u'pass', u'created_at': u'Tue, 26 Jul 2016 20:09:38 GMT', u'failure_details': u'', u'id': 3},
#                {u'status': u'pass', u'created_at': u'Tue, 26 Jul 2016 20:48:38 GMT', u'failure_details': u'', u'id': 4},
#                {u'status': u'pass', u'created_at': u'Tue, 26 Jul 2016 21:10:38 GMT', u'failure_details': u'', u'id': 5},
#                {u'status': u'pass', u'created_at': u'Tue, 26 Jul 2016 21:50:38 GMT', u'failure_details': u'', u'id': 6},
#                {u'status': u'pass', u'created_at': u'Tue, 26 Jul 2016 22:09:38 GMT', u'failure_details': u'', u'id': 7},
#                {u'status': u'pass', u'created_at': u'Tue, 26 Jul 2016 22:38:38 GMT', u'failure_details': u'', u'id': 8},
#                {u'status': u'pass', u'created_at': u'Tue, 26 Jul 2016 23:09:38 GMT', u'failure_details': u'', u'id': 9},
#                {u'status': u'pass', u'created_at': u'Tue, 26 Jul 2016 23:40:38 GMT', u'failure_details': u'',
#                 u'id': 10},
#                {u'status': u'pass', u'created_at': u'Tue, 27 Jul 2016 00:09:38 GMT', u'failure_details': u'',
#                 u'id': 11},
#                {u'status': u'pass', u'created_at': u'Tue, 27 Jul 2016 00:15:38 GMT', u'failure_details': u'',
#                 u'id': 12},
#                {u'status': u'pass', u'created_at': u'Tue, 27 Jul 2016 01:09:38 GMT', u'failure_details': u'',
#                 u'id': 13},
#                {u'status': u'pass', u'created_at': u'Tue, 27 Jul 2016 01:50:38 GMT', u'failure_details': u'',
#                 u'id': 14},
#                {u'status': u'pass', u'created_at': u'Tue, 27 Jul 2016 02:22:38 GMT', u'failure_details': u'',
#                 u'id': 15},
#                {u'status': u'pass', u'created_at': u'Tue, 27 Jul 2016 02:50:38 GMT', u'failure_details': u'',
#                 u'id': 16},
#                {u'status': u'pass', u'created_at': u'Tue, 27 Jul 2016 03:21:38 GMT', u'failure_details': u'',
#                 u'id': 17},
#                {u'status': u'pass', u'created_at': u'Tue, 27 Jul 2016 03:50:38 GMT', u'failure_details': u'',
#                 u'id': 18},
#                {u'status': u'pass', u'created_at': u'Tue, 27 Jul 2016 04:09:38 GMT', u'failure_details': u'',
#                 u'id': 19},
#                {u'status': u'fail', u'created_at': u'Tue, 27 Jul 2016 04:20:38 GMT', u'failure_details': u'', u'id': 20}
#
#                ]
#
#     interval = request.args.get('interval')
#     resolution = request.args.get('resolution')
#     threshold = request.args.get('threshold')
#     analysis_call = process_trend.delay(project_id=project_id, canary_id=canary_id, interval=interval,
#                                         resolution=resolution,
#                                         threshold=threshold, results=results)
#     results_list, values = analysis_call.wait()
#     line = pygal.Line()
#     line.title = "my awesome graph"
#     line.x_labels = values
#     line.add("status", [1 if x == "green"  else 0 for x in results_list])
#     return line.render()
    # return jsonify(msg="trending done")





#   TASK.PY
#
# worker_app = Celery("canary_analyzer", broker="redis://192.168.99.100:6379/0",
#                     backend="redis://192.168.99.100:6379/0",
#                     include=["app.worker.tasks"])
#
# analyzer = ThresholdAnalyzer()
# trend = TrendAnalyzer()
#
#
#
# @worker_app.task
# def process_canary(canary_id, project_id):
#     analyzer.process_canary(project_id=project_id, canary_id=canary_id)
#
#
# @worker_app.task
# def process_trend(project_id, canary_id, interval, resolution, threshold, results):
#     return trend.process_trend(project_id=project_id, canary_id=canary_id, interval=interval, resolution=resolution,
#                            threshold=threshold, results=results)

#
#





            # PROCESS TREND WITH IF STATEMENT (WORKS BUT NOT AS ROBUST)

# def process_trend(self, project_id, canary_id, interval, resolution, threshold, results):
#     # results = self.api_client.get_results(project_id=project_id, canary_id=canary_id, interval=interval, sample_size=None)
#     # results_list = results.get('results')
#     resolution = self.time_conversion(resolution)
#     status_list = []
#     length = len(results)
#     analysis_list = []
#     at_border = False
#     start_time = datetime.strptime(results[0].get('created_at'), '%a, %d %b %Y %H:%M:%S %Z')
#     border = start_time + resolution
#     for index in range(length):
#         if index != length - 1:
#             print results[index].get("id"), datetime.strptime(results[index].get('created_at'),
#                                                               '%a, %d %b %Y %H:%M:%S %Z')
#             if at_border:
#                 border = border + resolution
#                 at_border = False
#             if datetime.strptime(results[index].get('created_at'), '%a, %d %b %Y %H:%M:%S %Z') <= border:
#                 analysis_list.append(results[index].get('status'))
#             else:
#                 at_border = True
#                 status_list.append(self.trend_analyzer(threshold, analysis_list))
#                 analysis_list = []
#                 analysis_list.append(results[index].get('status'))
#         else:
#             analysis_list.append(results[index].get('status'))
#             status_list.append(self.trend_analyzer(threshold, analysis_list))
#     label = ["day1", "day2", "day3", "day4", "day5", "day6", "day7", "day8", "day9", "day10"]
#     print "STATUS LIST IS"
#     print status_list
#     return status_list, label
#







        # THIS IS PROCESS TREND THAT WORKS IN A ROBUST WAY:
        # credits: Holy Spirit!
# # Always clear your table after each call to trend
#     def process_trend(self, project_id, canary_id, interval, resolution, threshold):
#         gen.generate_test_results(project_id=project_id, canary_id=canary_id, interval=interval,count=10)
#         results = self.api_client.get_results(project_id=project_id, canary_id=canary_id, interval=interval, sample_size=None)
#         results_list = sorted(results.get('results'))
#         for result in results_list:
#             print result
#             print '\n'
#         resolution = self.time_conversion(resolution)
#         status_list = []
#         length = len(results_list)
#         analysis_list = []
#         example_list = []
#         start_time = datetime.strptime(results_list[0].get('created_at'), '%a, %d %b %Y %H:%M:%S %Z')
#         print "START TIME IS " , start_time
#         border = start_time + resolution
#         index = 0
#         labels = []
#         print "START TIME IS", start_time
#         while index < length:
#             print results_list[index].get("id"), datetime.strptime(results_list[index].get('created_at'),
#                                                               '%a, %d %b %Y %H:%M:%S %Z')
#             print "BORDER AT INDEX {index} is".format(index=index), border
#
#             if index != length - 1:
#                 if datetime.strptime(results_list[index].get('created_at'), '%a, %d %b %Y %H:%M:%S %Z') <= border:
#                     analysis_list.append(results_list[index].get('status'))
#                     example_list.append(self.Example(results_list[index].get('status'), results_list[index].get('id')))
#                     index += 1
#                 else:
#                     print example_list
#                     if analysis_list:
#                      print "BORDER", border

#                           labels.append(border - resolution)
#                         status_list.append(self.trend_analyzer(threshold, analysis_list))
#                         analysis_list = []
#                         example_list = []
#                     border = border + resolution
#             else:
#                 # created_at = datetime.strptime(results_list[index].get('created_at'), '%a, %d %b %Y %H:%M:%S %Z')
#                 if datetime.strptime(results_list[index].get('created_at'), '%a, %d %b %Y %H:%M:%S %Z') <= border:
#                       print "BORDER", border

#                     labels.append(border - resolution)
#                     analysis_list.append(results_list[index].get('status'))
#                     example_list.append(self.Example(results_list[index].get('status'), results_list[index].get('id')))
#                     status_list.append(self.trend_analyzer(threshold, analysis_list))
#                     print "LAAAAST ANALYSIS", example_list
#                 else:
#                       print "BORDER", border

#                     print "going to analyse ", example_list
#                     labels.append(border - resolution)
#                     status_list.append(self.trend_analyzer(threshold, analysis_list))
#                     analysis_list = []
#                     example_list = []
#                     border = border + resolution
#                     while True:
#                         print "BOOORDER IS", border
#                         if datetime.strptime(results_list[index].get('created_at'), '%a, %d %b %Y %H:%M:%S %Z') <= border:
#                              print "BORDER", border

#                             analysis_list.append(results_list[index].get('status'))
#                             labels.append(border - resolution)
#                             example_list.append(self.Example(results_list[index].get('status'), results_list[index].get('id')))
#                             status_list.append(self.trend_analyzer(threshold, analysis_list))
#                             print "LAST ANALYSIS", example_list
#                             break
#                         else:
#                             border = border + resolution
#                 index += 1
#
#          for label in labels:
#             print label
#             print '\n'
#         print "STATUS LIST IS"
#         print status_list
#         return status_list, label



#
# class Example():
#     def __init__(self, status, id):
#         self.status = status
#         self.id = id
#
#     def __repr__(self):
#         return "[id = %d, status = %s]" % (self.id, self.status)



# check range to be good when there is no 100% pass
# line breaks on None data
# Architecture
# demo


#
#
# def format_datetime(values, resolution):
#     value = resolution.split()
#     format_values = []
#     if value[1] == "days":
#         for timee in values:
#             format_values.append(datetime.strptime(timee, '%Y-%m-%d'))
#         return format_values
#     elif value[1] == "hours":
#         for timee in values:
#             # timee = str.join(' ', timee.split('.')[0:1])
#             # n_time = datetime.strptime(timee, '%Y-%m-%d %H:%M:%S')
#             format_values.append(n_time)
#         return format_values

#
#
#
# line.y_labels = [
#     {
#         'value': 3,
#         'label': ''
#     },
#     {
#         'value': 2,
#         'label': 'Green',
#         'color': 'green'
#     },
#     {
#         'value': 1,
#         'label': 'Red',
#         'color': 'red'
#     },
#     {
#         'value': 0,
#         'label': ''
#     }
# ]
# line.add('Health', [2 if x == "GREEN" else 1 for x in health_list])
#
# return line.render()


#  NOT REALLY WORKING
# def process_trend(self, resolution, threshold, interval, start_time):
#     results_list = sorted(results)
#     for res in results_list:
#         print res
#         print '\n'
#
#     resolution = self.time_conversion(resolution)
#     status_list = []
#     length = len(results_list)
#     analysis_list = []
#     time_format = '%Y-%m-%d %H:%M:%S.%f'
#     interval = self.time_conversion(interval)
#     border = start_time - interval + resolution
#     index = 0
#     labels = []
#     my_list = []
#     while index < length:
#         created_at = datetime.strptime(results_list[index].
#                                        get('created_at'),
#                                        time_format)
#         print "BORDER AT INDEX {} IS {}".format(index, border)
#         if created_at <= border:
#             analysis_list.append(results_list[index].get('status'))
#             my_list.append(self.Example(results_list[index].get('status'),
#                                         results_list[index].get('id')))
#         else:
#             labels.append("{}".format(border - resolution))
#             result = self.trend_analyzer(threshold, analysis_list)
#             status_list.append(result)
#             print "INSIDE THE ELSE", my_list
#             analysis_list = []
#             my_list = []
#             analysis_list.append(results_list[index].get('status'))
#             my_list.append(self.Example(results_list[index].get('status'),
#                                         results_list[index].get('id')))
#             border = border + resolution
#
#         if index == length - 1:
#             labels.append("{}".format(border - resolution))
#             result = self.trend_analyzer(threshold, analysis_list)
#             status_list.append(result)
#             print "FINALLY", my_list
#
#         index += 1
#
#     print "STATUS LIST IS", status_list
#     print "LABELS IS ", labels
#     return status_list, labels











# def process_trend(self, resolution, threshold, interval, start_time):
#     results_list = sorted(results)
#     resolution = self.time_conversion(resolution)
#     status_list = []
#     length = len(results_list)
#     analysis_list = []
#     example_list = []
#     for result in results_list:
#         print result
#         print '\n'
#     interval = self.time_conversion(interval)
#     border = start_time - interval + resolution
#     print "START TIME IS", start_time
#     print "INTERVAL IS", interval
#     print "RESOLUTION IS", resolution
#     print "START BORDER IS", border
#     index = 0
#     labels = []
#     while index < length:
#         print "BORDER AT INDEX {} IS {}".format(index, border)
#         if index != length - 1:
#             created_at = datetime.strptime(
#                 results_list[index].get('created_at'),
#                 '%Y-%m-%d %H:%M:%S.%f')
#             if created_at <= border:
#                 analysis_list.append(results_list[index].get('status'))
#                 example_list.append(
#                     self.Example(results_list[index].get('status'),
#                                  results_list[index].get('id')))
#                 index += 1
#             else:
#                 # at a border
#                 labels.append("{}".format(border - resolution))
#                 status_list.append(
#                     self.trend_analyzer(analysis_list))
#                 print "ANALYSING....", example_list
#                 analysis_list = []
#                 example_list = []
#                 border = border + resolution
#         else:
#             # looking at the last result
#             created_at = datetime.strptime(
#                 results_list[index].get('created_at'),
#                 '%Y-%m-%d %H:%M:%S.%f')
#             if created_at <= border:
#                 # if last result is in the same time resolution as the previous
#                 labels.append("{}".format(border - resolution))
#                 analysis_list.append(results_list[index].get('status'))
#                 example_list.append(
#                     self.Example(results_list[index].get('status'),
#                                  results_list[index].get('id')))
#                 status_list.append(self.trend_analyzer(analysis_list))
#                 print "ANALYSING LAST WITH GROUP", example_list
#             else:
#                 # analyse what you currently have and try to get the last result in the right time frame
#                 labels.append("{}".format(border - resolution))
#                 status_list.append(self.trend_analyzer(analysis_list))
#                 print "ANALYSING LAST W/OUT GROUP", example_list
#                 analysis_list = []
#                 example_list = []
#                 border = border + resolution
#                 while True:
#                     if created_at <= border:
#                         labels.append("{}".format(border - resolution))
#                         analysis_list.append(
#                             results_list[index].get('status'))
#                         example_list.append(
#                             self.Example(results_list[index].get('status'),
#                                          results_list[index].get('id')))
#                         status_list.append(
#                             self.trend_analyzer(analysis_list))
#                         break
#                     else:
#                         border = border + resolution
#             index += 1
#     print "STATUS LIST IS", status_list
#     print "LABELS IS ", labels
#     return status_list, labels
#
#
# def trend_analyzer(self, results_list):
#     if len(results_list) == 0:
#         return 1
#     else:
#         passes = 0
#         fails = 0
#         for result in results_list:
#             if result == 'pass':
#                 passes += 1
#             else:
#                 fails += 1
#         assert len(results_list) == (passes + fails)
#         pass_percent = passes / len(results_list) * 100
#         return pass_percent
#

















# ierhejplq

# def process_trend(self, resolution, threshold, interval, start_time):
#     results_list = sorted(results)
#     resolution = self.time_conversion(resolution)
#     status_list = []
#     length = len(results_list)
#     analysis_list = []
#     example_list = []
#     for result in results_list:
#         print result
#         print '\n'
#     interval = self.time_conversion(interval)
#     border = start_time - interval + resolution
#     print "START TIME IS", start_time
#     print "INTERVAL IS", interval
#     print "RESOLUTION IS", resolution
#     print "START BORDER IS", border
#     index = 0
#     labels = []
#     while index < length:
#         print "BORDER AT INDEX {} IS {}".format(index, border)
#         created_at = datetime.strptime(
#             results_list[index].get('created_at'),
#             '%Y-%m-%d %H:%M:%S.%f')
#         if created_at <= border:
#             analysis_list.append(results_list[index].get('status'))
#             example_list.append(self.Example(results_list[index].get('status'),
#                                              results_list[index].get('id')))
#             index += 1
#         else:
#             # at a border
#             labels.append("{}".format(border - resolution))
#             status_list.append(
#                 self.trend_analyzer(analysis_list))
#             print "ANALYSING....", example_list
#             analysis_list = []
#             example_list = []
#             border = border + resolution
#
#         if index == length - 1:
#             # looking at the last result
#             created_at = datetime.strptime(
#                 results_list[index].get('created_at'),
#                 '%Y-%m-%d %H:%M:%S.%f')
#             if created_at <= border:
#                 # if last result is in the same time resolution as the previous
#                 labels.append("{}".format(border - resolution))
#                 analysis_list.append(results_list[index].get('status'))
#                 example_list.append(
#                     self.Example(results_list[index].get('status'),
#                                  results_list[index].get('id')))
#                 status_list.append(self.trend_analyzer(analysis_list))
#                 print "ANALYSING LAST WITH GROUP", example_list
#             else:
#                 # analyse what you currently have and try to get the last result in the right time frame
#                 labels.append("{}".format(border - resolution))
#                 status_list.append(self.trend_analyzer(analysis_list))
#                 print "ANALYSING LAST W/OUT GROUP", example_list
#                 analysis_list = []
#                 example_list = []
#                 border = border + resolution
#                 while True:
#                     if created_at <= border:
#                         labels.append("{}".format(border - resolution))
#                         analysis_list.append(
#                             results_list[index].get('status'))
#                         example_list.append(
#                             self.Example(results_list[index].get('status'),
#                                          results_list[index].get('id')))
#                         status_list.append(
#                             self.trend_analyzer(analysis_list))
#                         break
#                     else:
#                         border = border + resolution
#             index += 1
#     print "STATUS LIST IS", status_list
#     print "LABELS IS ", labels
#     return status_list, labels



# def x_value_formatter(values):
#     time_list = []
#     for value in values:
#         time_list.append(value[0:10] + ' at' + value[10:16])
#     return time_list