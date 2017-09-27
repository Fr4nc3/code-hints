# *************************************
# @Fr4nc3
# file: projectile.py
# implement methods
# g(h)
# s_next ( s_current, v_current, delta_t)
# v_next(s_next, v_current, delta_t)
# s_sim(t, v_init, s_init, delta_t)
# s_standard(t,v_init)
# *************************************
GRAVITATIONAL_CONSTANT = 6.6742e-11  # gravitational constant in N*(m/kg)2
ME = 5.9736e24  # mass of the earth
RE = 6.371e6  # radius of the earth


def g(h):
    H = RE + h
    const = GRAVITATIONAL_CONSTANT * ME
    if H != 0:  # avoid division by zero
        return const / H ** 2
    else:
        return const / RE ** 2  # ignoring h


def s_next(s_current, v_current, delta_t):
    ''' Implements eq: s(t+∆t) = s(t) + v(t)∙∆t '''
    return s_current + v_current * delta_t


def v_next(s_next, v_current, delta_t):
    ''' Implements v(t+∆t) = v(t) - g(s(t+∆t)) ∙ ∆t '''
    # s_next is already calculated used s_next()
    return v_current - g(s_next) * delta_t


def s_sim(t, v_0, s_0, delta_t):
    ''' Implements simulated position
    note: this was the only way that s_sim can uses methods g, v_next,
    and s_next at the same time '''
    s_n = s_next(s_0, v_0, delta_t)  # get the s_next
    v_n = v_next(s_n, v_0, delta_t)  # uses s_next to calculate v_next
    return -0.5 * g(s_n) * t ** 2 + v_n * t


def s_standard(t, v_0):
    # calculate position assuming h is 0 witch g~9.8
    return -0.5 * g(0) * t ** 2 + v_0 * t



