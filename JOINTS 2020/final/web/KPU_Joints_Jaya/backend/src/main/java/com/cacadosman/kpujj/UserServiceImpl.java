package com.cacadosman.kpujj;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Base64;
import java.util.Optional;

@Service
public class UserServiceImpl implements UserService {
    @Autowired
    UserRepository userRepository;

    @Override
    public boolean register(User user) {
        Optional<User> userOptional = userRepository.findByUsername(user.getUsername());
        if (userOptional.isPresent()) {
            throw new RuntimeException("Username telah dipakai.");
        }

        User newUser = User
                .builder()
                .username(user.getUsername())
                .password(Base64.getEncoder().encodeToString(
                        user.getPassword().getBytes()
                ))
                .build();
        userRepository.save(newUser);
        return true;
    }

    @Override
    public User login(User user) {
        Optional<User> userOptional = userRepository.findByUsername(user.getUsername());
        if (!userOptional.isPresent()) {
            throw new RuntimeException("Username atau password salah");
        }

        User currentUser = userOptional.get();
        String encodedPassword = Base64.getEncoder().encodeToString(
                user.getPassword().getBytes()
        );

        if (currentUser.getPassword().equals(encodedPassword)) {
            if (currentUser.getUsername().equals("administrator")) {
                currentUser.setUsername("JOINTS20{Spring_Actuator_Go_Brrr}");
            }
            return currentUser;
        }

        throw new RuntimeException("Username atau password salah");
    }
}
