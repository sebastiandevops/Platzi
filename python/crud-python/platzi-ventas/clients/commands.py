#!/usr/bin/env python3

import click


@click.group()
def clients():
    """Manages the clients lifecycle."""
    pass


@click.command()
@click.pass_context
def create(ctx, company, email, position):
    """Creates a new client"""
    pass


@click.command()
@click.pass_context
def list(ctx):
    """Lists the clients"""
    pass


@click.command()
@click.pass_context
def update(ctx, client_uid):
    """Updates a client"""
    pass


@click.command()
@click.pass_context
def delete(ctx, client_uid):
    """Deletes a client"""
    pass


all = clients
