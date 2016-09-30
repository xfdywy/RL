% exact DP - VI
% finite time binomial call option

clc
clear

%%% Varaibles %%%

% n - number of states
% T  - horizon
% J  - n x T matrix
% policy - n x T matrix

% J(i,t)      - the value function at time t and state i
% policy(i,t) - the policy at time t and state i, 
              % 1: Exercise, 2: Hold


%%% Parameters %%%

K = 1;      % Strike Price
S = 1;      % Initial Price
p = 0.495;  % Probability of Moving Up
u = 1.01;   % Growth Rate
d = 0.9;    % Diminish Rate
T = 1000;   % Horizon, or Duration
n = 100;    % Number of States
alpha = 1;  % Discount Factor
 
r = u;

price_list = S*[d.^((n/2-1):-1:0), u.^(1:(n/2))]; % List of All Possible States

%%% Initialization %%%
J = zeros(n,T);
policy = ones(n,T); % 1 - Exercise, 2 - Hold

% Cost vector at time T
J(:,T) = max(price_list-K, zeros(1,n))'; 

%% DP Algorithm
for t = (T-1):-1:1
    
    for i = 1:n
        %% Write the one-step-backward DP algorithm here:
        
        
    end

end

%% Plot the Option Prices and Exercising Strategies

figure(1)
surf(1:100,price_list,policy(:,T/100*(1:100)));ylabel('Stock Price');xlabel('Time');
view(0, 90);
title('Optimal Exercising Policy (blue: exercise, red: hold)');
%print(1,'exact-finite-policy-2','-depsc')

figure(2)
surf(1:100,price_list,J(:,T/100*(1:100)));ylabel('Stock Price');xlabel('Time');
title('Optimal Value Fucntion (Option Price at given time and stock price)');
%print(2,'exact-finite-J-2','-depsc')
