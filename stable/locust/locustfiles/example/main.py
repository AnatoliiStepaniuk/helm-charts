# -*- coding: utf-8 -*-

from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def call_a(self):
        self.client.get("/a")
