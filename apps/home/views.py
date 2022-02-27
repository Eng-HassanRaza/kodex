# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import os

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import base64
import requests
from django.templatetags.static import static

from urllib.parse import urlparse

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    if request.method == 'POST':
        results = []
        github_api = "https://api.github.com/repos"
        url = request.POST["github-repo"]
        dir = request.POST["github-repo-dir"]
        clean_url = urlparse(url).path.strip("/").split("/")
        repo_user = clean_url[0]
        repo_name = clean_url[1]
        api_url = f"{github_api}/{repo_user}/{repo_name}/contents/{dir}"
        req = requests.get(api_url)
        json_response = req.json()
        url = url.replace('/tree', '')
        for file in json_response:
            results_file={}
            name = file["path"]
            file_name = file["name"]
            page = requests.get(url+"/tree/main/" + name)
            if page.status_code == requests.codes.ok:
                dense = page.text.count("Dense") - 1
                relu = page.text.count("relu")
                sigmoid = page.text.count("sigmoid")
                results_file={"filename":file_name,"dense":dense,"relu":relu,"sigmoid":sigmoid}
            results.append(results_file)
        context={"resluts":results}
    html_template = loader.get_template('home/home.html')
    return HttpResponse(html_template.render(context, request))
