from django.shortcuts import render
from subprocess import run , PIPE 
from rest_framework.views import APIView
from rest_framework.response import Response


import subprocess
from django.http import JsonResponse ,StreamingHttpResponse

from django.views.decorators.csrf import csrf_exempt

import subprocess
from django.http import JsonResponse
import base64,  json
# from rest_framework import APIView


@csrf_exempt
# class ObjectDetectionView122(APIView):
  
def ObjectDetectionView(request):
        if request.method == 'POST':
            default_camera = int(request.POST.get('defaultCameraIndex').strip("'"))
            command = f'python detect.py --source {default_camera}'

            # Run the command to perform object detection
            result = run(command, shell=True, check=True, cwd=r'detectobject\yolov7', stdout=PIPE, stderr=PIPE)
            # Process the output to extract im0 and s
            output_lines = result.stdout.decode().split('\n')
            s = None
            base64_str = None
            for line in output_lines:
                if line.startswith('seem'):
                    s = line[len('seem'):].strip()
                if line.startswith('byte'):
                    base64_str = line[len('byte'):]

            response_data = {
                's': s,
                'base64_str': base64_str
            }
            return StreamingHttpResponse(json.dumps(response_data) + '\n', content_type='text/event-stream')
        
            # return JsonResponse(response_data, safe=False)
        
        elif request.method == 'GET':
            default_camera = request.GET.get('source', '0')
            command = f'python detect.py --source {default_camera}'

            # Run the command to perform object detection
            result = run(command, shell=True, check=True, cwd=r'detectobject\yolov7', stdout=PIPE, stderr=PIPE)

            # Process the output to extract im0 and s
            output_lines = result.stdout.decode().split('\n')
            s = None
            base64_str = None
            for line in output_lines:
                if line.startswith('seem'):
                    s = line[len('seem'):].strip()
                if line.startswith('byte'):
                    base64_str = line[len('byte'):]
          

            response_data = {
                's': s,
                'base64_str': base64_str
            }
            return StreamingHttpResponse(json.dumps(response_data) + '\n', content_type='text/event-stream')

        else:
            return JsonResponse({"status": "error", "message": "Invalid request method."})


@csrf_exempt
def api2(request):
    return ObjectDetectionView(request)

##################################    
# # class ObjectDetectionView(APIView):
    
# def ObjectDetectionView( request):
        
#         if request.method == 'POST':
#             default_camera = int(request.POST.get('defaultCameraIndex').strip("'"))
            
#             # Get the camera source value from the request
#             # camera_source = request.GET.get('source', '0')  # Default value is '0' if not provided in the request
#             # detect_path = r'project\detectobject\yolov7-main\detect.py'
#             command = f'python detect.py --source {default_camera}'

#             # Build the command to run the modified detect.py script
#             # command = f'python detect.py --source {camera_source}'
            

#             # Run the command to perform object detection
#             run(command, shell=True, check=True, cwd=r'detectobject\yolov7')  # Adjust the paths accordingly

#             # Process the object detection results
#             # (you can modify this part to handle the output of the detect.py script)
#             # res = detect()
            
#             # Return the object detection results as JSON
#             return Response({"status": "success", "message":'detect'})
#             # return default_camera
#         elif request.method == 'GET':
#             default_camera =  request.GET.get('source', '0')
                   
#             # Get the camera source value from the request
#             # camera_source = request.GET.get('source', '0')  # Default value is '0' if not provided in the request
#             # detect_path = r'project\detectobject\yolov7-main\detect.py'
#             command = f'python detect.py --source {0}'

#             # Run the command to perform object detection
#             run(command, shell=True, check=True, cwd=r'detectobject\yolov7')  # Adjust the paths accordingly

#             # Process the object detection results
#             # (you can modify this part to handle the output of the detect.py script)
            
#             # Return the object detection results as JSON
#             return Response({"status": "success", "message": "Object detection completed."})
#             # return HttpResponse(default_camera)
#             # return default_camera
#         else:
#         # Code to handle other types of requests
#         # return HttpResponse('Unsupported request method')
#             return ('None')
        
        
#######################
        
        # # Get the camera source value from the request
        # # camera_source = request.GET.get('source', '0')  # Default value is '0' if not provided in the request
        # # detect_path = r'project\detectobject\yolov7-main\detect.py'
        # command = f'python detect.py --source {default_camera}'

        # # Build the command to run the modified detect.py script
        # # command = f'python detect.py --source {camera_source}'
        

        # # Run the command to perform object detection
        # run(command, shell=True, check=True, cwd=r'detectobject\yolov7')  # Adjust the paths accordingly

        # # Process the object detection results
        # # (you can modify this part to handle the output of the detect.py script)

        # # Return the object detection results as JSON
        # return Response({"status": "success", "message": "Object detection completed."})



        